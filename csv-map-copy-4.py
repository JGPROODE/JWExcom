import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os
import shutil

class FolderGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Generator")

        # Frame voor CSV-bestand
        self.csv_frame = tk.Frame(root)
        self.csv_frame.pack(pady=10)

        tk.Label(self.csv_frame, text="Selecteer het CSV-bestand:").grid(row=0, column=0, sticky="w")
        self.csv_entry = tk.Entry(self.csv_frame, width=50)
        self.csv_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.csv_frame, text="Bladeren", command=self.browse_csv).grid(row=0, column=2)

        # Frame voor documentenmap
        self.documents_frame = tk.Frame(root)
        self.documents_frame.pack(pady=10)

        tk.Label(self.documents_frame, text="Selecteer de map met documenten:").grid(row=0, column=0, sticky="w")
        self.documents_entry = tk.Entry(self.documents_frame, width=50)
        self.documents_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.documents_frame, text="Bladeren", command=self.browse_documents).grid(row=0, column=2)

        # Actieknop
        tk.Button(root, text="Genereer mappen", command=self.generate_folders).pack(pady=20)

    def browse_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV-bestanden", "*.csv")])
        self.csv_entry.delete(0, tk.END)
        self.csv_entry.insert(0, file_path)

    def browse_documents(self):
        folder_path = filedialog.askdirectory()
        self.documents_entry.delete(0, tk.END)
        self.documents_entry.insert(0, folder_path)

    def generate_folders(self):
        csv_path = self.csv_entry.get()
        documents_path = self.documents_entry.get()

        if not csv_path or not documents_path:
            tk.messagebox.showwarning("Waarschuwing", "Selecteer zowel het CSV-bestand als de map met documenten.")
            return

        try:
            # Lees het CSV-bestand in een DataFrame
            df = pd.read_csv(csv_path)

            # Itereer over elke rij in het DataFrame
            for index, row in df.iterrows():
                studentnummer = str(row["Studentnummer"])
                achternaam = str(row['Achternaam'])
                voorvoegsel = str(row['Voorvoegsel']) if not pd.isna(row['Voorvoegsel']) else ""
                voorletters = str(row['Voorletters'])
                opleiding = str(row['Opleiding'])
                cohort = str(row['Cohort'])

                # Maak de mapnaam
                folder_name = f"{opleiding}/{achternaam}-{voorvoegsel}-{voorletters}-{studentnummer}"

                # Volledig pad naar de nieuwe map
                new_folder_path = os.path.join("C:/", folder_name)

                # Maak de map aan
                os.makedirs(new_folder_path, exist_ok=True)

                # Kopieer bestanden naar de nieuwe map
                for filename in os.listdir(documents_path):
                    source_path = os.path.join(documents_path, filename)
                    destination_path = os.path.join(new_folder_path, f"{studentnummer}-{filename}")
                    shutil.copy2(source_path, destination_path)

            tk.messagebox.showinfo("Succes", "Mappen zijn succesvol gegenereerd.")
        except Exception as e:
            tk.messagebox.showerror("Fout", f"Er is een fout opgetreden:\n{str(e)}")

# Hoofdprogramma
if __name__ == "__main__":
    root = tk.Tk()
    app = FolderGeneratorApp(root)
    root.mainloop()
