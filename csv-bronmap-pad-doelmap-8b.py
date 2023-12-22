import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd


class FileMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bestandsverplaatsingstool")

        self.csv_file_path = tk.StringVar()
        self.source_folder = tk.StringVar()

        # Nieuwe variabelen voor het bewaren van de geselecteerde kolommen
        self.selected_path_columns = []
        self.selected_name_columns = []

        # GUI-elementen
        tk.Label(root, text="Pad naar CSV-bestand:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.csv_file_path, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(root, text="Blader...", command=self.browse_csv).grid(row=0, column=2, padx=10, pady=10)

        tk.Label(root, text="Pad naar bronmap:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.source_folder, width=50).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(root, text="Blader...", command=self.browse_source).grid(row=1, column=2, padx=10, pady=10)

        tk.Button(root, text="Lees CSV-bestand", command=self.read_csv).grid(row=2, column=1, pady=10)

        tk.Label(root, text="Selecteer padkolommen:").grid(row=3, column=0, padx=10, pady=10)
        self.path_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, exportselection=0)
        self.path_listbox.grid(row=4, column=0, padx=10, pady=10)

        tk.Label(root, text="Selecteer naamkolommen:").grid(row=3, column=1, padx=10, pady=10)
        self.name_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, exportselection=0)
        self.name_listbox.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(root, text="Verplaats bestanden", command=self.move_files).grid(row=5, column=1, pady=20)

    def browse_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV-bestanden", "*.csv")])
        self.csv_file_path.set(file_path)

    def browse_source(self):
        folder_path = filedialog.askdirectory()
        self.source_folder.set(folder_path)

    def read_csv(self):
        csv_file_path = self.csv_file_path.get()
        if not os.path.isfile(csv_file_path):
            messagebox.showerror("Fout", "Selecteer eerst een geldig CSV-bestand.")
            return

        try:
            # Geef de puntkomma aan als scheidingsteken
            df = pd.read_csv(csv_file_path, sep=';', na_values=[''], keep_default_na=False)
        except Exception as e:
            messagebox.showerror("Fout", f"Fout bij het lezen van CSV-bestand:\n{e}")
            return

        # Verwijder lege kolommen
        df = df.dropna(axis=1, how='all')

        # Toon kolomkeuze na het inlezen van het CSV-bestand
        self.update_listbox(self.path_listbox, df.columns)
        self.update_listbox(self.name_listbox, df.columns)

        # Bewaar de geselecteerde kolommen
        self.selected_path_columns = []
        self.selected_name_columns = []

    def update_listbox(self, listbox, column_names):
        listbox.delete(0, tk.END)
        for name in column_names:
            listbox.insert(tk.END, name)

    def move_files(self):
        csv_file_path = self.csv_file_path.get()
        source_folder = self.source_folder.get()

        if not os.path.isfile(csv_file_path) or not os.path.isdir(source_folder):
            messagebox.showerror("Fout", "Ongeldige bestands- of maplocatie.")
            return

        path_indices = self.path_listbox.curselection()
        name_indices = self.name_listbox.curselection()

        if not path_indices:
            messagebox.showerror("Fout", "Selecteer minstens één kolom voor het pad.")
            return

        if not name_indices:
            messagebox.showerror("Fout", "Selecteer minstens één kolom voor de bestandsnaam.")
            return

        # Bewaar de geselecteerde kolommen
        self.selected_path_columns = [self.path_listbox.get(idx) for idx in path_indices]
        self.selected_name_columns = [self.name_listbox.get(idx) for idx in name_indices]

        # Lees het CSV-bestand
        df = pd.read_csv(csv_file_path, sep=';', na_values=[''], keep_default_na=False)

        # Loop over elk bestand in de bronmap en kopieer het naar de doelmap
        for _, row in df.iterrows():
            # Maak het pad op basis van de geselecteerde kolommen en volgorde
            destination_path = os.path.join("C:\\testdoel", *[str(row[name]) for name in self.selected_path_columns])

            # Maak de mapnaam op basis van de geselecteerde kolommen en volgorde
            folder_name_parts = [str(row[name]) for name in self.selected_name_columns]
            folder_name = "_".join(folder_name_parts)

            # Voeg de mapnaam toe aan het pad
            destination_path = os.path.join(destination_path, folder_name)
            self.create_directory(destination_path)

            # Kopieer alle bestanden in de bronmap naar de doelmap
            for filename in os.listdir(source_folder):
                source_file = os.path.join(source_folder, filename)
                
                # Pas de bestandsnaam aan op basis van de geselecteerde kolommen en volgorde
                file_name_parts = [str(row[name]) for name in self.selected_name_columns]
                destination_file = os.path.join(destination_path, "_".join(file_name_parts) + os.path.splitext(filename)[1])
                
                # Kopieer het bestand naar de doelmap met de nieuwe bestandsnaam
                shutil.copy2(source_file, destination_file)

        messagebox.showinfo("Voltooid", "Bestanden zijn verplaatst!")

    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileMoverApp(root)
    root.mainloop()
