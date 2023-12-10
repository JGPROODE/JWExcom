import os
import csv
import shutil
import pandas as pd
import tkinter as tk
from tkinter import ttk

class FileMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bestandsverplaatsingstool")

        self.csv_file_path = tk.StringVar()
        self.source_folder = tk.StringVar()
        self.selected_columns = tk.StringVar()

        # GUI-elementen
        tk.Label(root, text="Pad naar CSV-bestand:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.csv_file_path, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(root, text="Blader...", command=self.browse_csv).grid(row=0, column=2, padx=10, pady=10)

        tk.Label(root, text="Pad naar bronmap:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.source_folder, width=50).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(root, text="Blader...", command=self.browse_source).grid(row=1, column=2, padx=10, pady=10)

        tk.Label(root, text="Selecteer kolommen (gescheiden door komma's):").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.selected_columns, width=50).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(root, text="Selecteer kolommen en verplaats bestanden", command=self.move_files).grid(row=3, column=1, pady=20)

    def browse_csv(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("CSV-bestanden", "*.csv")])
        self.csv_file_path.set(file_path)

    def browse_source(self):
        folder_path = tk.filedialog.askdirectory()
        self.source_folder.set(folder_path)

    def move_files(self):
        csv_file_path = self.csv_file_path.get()
        source_folder = self.source_folder.get()

        if not os.path.isfile(csv_file_path) or not os.path.isdir(source_folder):
            tk.messagebox.showerror("Fout", "Ongeldige bestands- of maplocatie.")
            return

        # Lees het CSV-bestand in een pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Vraag de gebruiker om maximaal 6 kolomnamen te selecteren
        selected_columns = self.selected_columns.get().split(',')
        selected_columns = [col.strip() for col in selected_columns][:6]

        for index, row in df.iterrows():
            # Maak de doelmap
            destination_folder = os.path.join("C:", *row[selected_columns].astype(str))
            self.create_directory(destination_folder)

            # Kopieer de bestanden naar de doelmap
            self.copy_files(source_folder, destination_folder)

        tk.messagebox.showinfo("Voltooid", "Bestanden zijn verplaatst!")

    def create_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def copy_files(self, source, destination):
        for file_name in os.listdir(source):
            source_file = os.path.join(source, file_name)
            destination_file = os.path.join(destination, file_name)
            shutil.copy2(source_file, destination_file)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileMoverApp(root)
    root.mainloop()
