import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class FileMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bestandsverplaatsingstool")
        
    def browse_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV-bestanden", "*.csv")])
        self.csv_file_path.set(file_path)
        return file_path  # Toegevoegde returnwaarde

    def browse_source(self):
        folder_path = filedialog.askdirectory()
        self.source_folder.set(folder_path)
        return folder_path  # Toegevoegde returnwaarde

    def read_csv(self):
        csv_file_path = self.csv_file_path.get()
        if not os.path.isfile(csv_file_path):
            messagebox.showerror("Fout", "Selecteer eerst een geldig CSV-bestand.")
            return None  # Toegevoegde returnwaarde

        try:
            # Geef de puntkomma aan als scheidingsteken
            df = pd.read_csv(csv_file_path, sep=';', na_values=[''], keep_default_na=False)
        except Exception as e:
            messagebox.showerror("Fout", f"Fout bij het lezen van CSV-bestand:\n{e}")
            return None  # Toegevoegde returnwaarde

        # Verwijder lege kolommen
        df = df.dropna(axis=1, how='all')

        # Toon kolomkeuze na het inlezen van het CSV-bestand
        self.update_listbox(self.path_listbox, df.columns)
        self.update_listbox(self.name_listbox, df.columns)
        self.update_listbox(self.prefix_listbox, df.columns)

        # Bewaar de geselecteerde kolommen
        self.selected_path_columns = []
        self.selected_name_columns = []
        self.selected_prefix_columns = []
        return df  # Toegevoegde returnwaarde

    def move_files(self):
        # ... (andere bewerkingen)

        return result  # Toegevoegde returnwaarde

# ... (andere methoden)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileMoverApp(root)
    root.mainloop()
