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

def read_csv(self):
        csv_file_path = self.csv_file_path.get()
        if not os.path.isfile(csv_file_path):
            messagebox.showerror("Fout", "Selecteer eerst een geldig CSV-bestand.")
            return

        try:
            # Geef de puntkomma aan als scheidingsteken
            df = pd.read_csv(csv_file_path, sep=';')
        except Exception as e:
            messagebox.showerror("Fout", f"Fout bij het lezen van CSV-bestand:\n{e}")
            return

        # Toon kolomkeuze na het inlezen van het CSV-bestand
        self.update_listbox(self.path_listbox, df.columns)
        self.update_listbox(self.name_listbox, df.columns)





def move_files(self):
    # ... (eerder code)

    for index, row in df.iterrows():
        # Maak het pad
        destination_path = os.path.join("C:", *[str(row[name]) for name in path_columns])
        self.create_directory(destination_path)

        # Kopieer het bestand naar de doelmap met de nieuwe bestandsnaam
        file_name_parts = [str(row[name]) for name in name_columns]
        destination_file = os.path.join(destination_path, "-".join(file_name_parts))
        source_file = os.path.join(source_folder, str(row[name_columns[-1]]))
        shutil.copy2(source_file, destination_file)

    # ... (rest van de code)



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

    path_columns = [self.path_listbox.get(idx) for idx in path_indices]
    name_columns = [self.name_listbox.get(idx) for idx in name_indices]

    # Maak een map voor elke rij in het CSV-bestand
    df = pd.read_csv(csv_file_path, sep=';')
    for index, row in df.iterrows():
        # Maak het pad
        destination_path = os.path.join("C:", *[str(row[name]) for name in path_columns])
        self.create_directory(destination_path)

        # Kopieer het bestand naar de doelmap met de nieuwe bestandsnaam
        try:
            file_name_parts = [str(row[name]) for name in name_columns]
            destination_file = os.path.join(destination_path, "-".join(file_name_parts))
            source_file = os.path.join(source_folder, str(row[name_columns[-1]]))
            shutil.copy2(source_file, destination_file)
        except FileNotFoundError as e:
            print(f"Fout bij kopiëren van bestand: {e}")

    messagebox.showinfo("Voltooid", "Bestanden zijn verplaatst!")


