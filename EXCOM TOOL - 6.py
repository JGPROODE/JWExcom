import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import fitz  # PyMuPDF

# Constanten voor kleuren
APP_BACKGROUND_COLOR = '#FF0000'  # Knalrood
FRAME_BACKGROUND_COLOR = '#00FF00'  # Lichtgroen
BUTTON_BACKGROUND_COLOR = '#228B22'  # Donkergroen
BUTTON_TEXT_COLOR = '#FFFFFF'  # White
TITLE_BAR_BACKGROUND_COLOR = '#FFFF00'  # Geel
TITLE_BAR_TEXT_COLOR = '#FF0000'  # Rood
CSV_BUTTON_BLINK_COLOR = '#FF0000'  # Rood
HELP_BUTTON_COLOR = '#0000FF'  # Blauw

class CustomTitleBar(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg=kwargs.get('background', None))
        self.pack(fill='x')
        label = tk.Label(self, text="J.G.P. Roode: \"Lees CSV, Maak Doelpad, Prefix voor mapnaam en verplaats de bestanden uit de BronMap- tool\" ",
                         background=kwargs.get('background', None), foreground=kwargs.get('foreground', None))
        label.pack(fill='x')

class FileMoverApp:
    def __init__(self, root, initial_csv_path=None, initial_source_folder=None):
        self.root = root
        self.root.title("J.G.P. Roode: \"Lees CSV, Maak Doelpad, Prefix voor mapnaam en verplaats de bestanden uit de BronMap- tool\" ")

        # Gele achtergrond met rode letters voor de titelbalk
        self.title_bar = CustomTitleBar(root, background=TITLE_BAR_BACKGROUND_COLOR, foreground=TITLE_BAR_TEXT_COLOR)

        self.csv_file_path = tk.StringVar()
        self.source_folder = tk.StringVar()

        self.selected_path_columns = []
        self.selected_name_columns = []
        self.selected_prefix_columns = []

        tk.Label(root, text="Pad naar CSV-bestand:", bg=APP_BACKGROUND_COLOR).grid(row=0, column=0, padx=10, pady=10, sticky='e')
        tk.Entry(root, textvariable=self.csv_file_path, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(root, text="Blader...", command=self.browse_csv, bg=BUTTON_BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR).grid(row=0, column=2, padx=10, pady=10)

        tk.Label(root, text="Pad naar bronmap:", bg=APP_BACKGROUND_COLOR).grid(row=1, column=0, padx=10, pady=10, sticky='e')
        tk.Entry(root, textvariable=self.source_folder, width=50).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(root, text="Blader...", command=self.browse_source, bg=BUTTON_BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR).grid(row=1, column=2, padx=10, pady=10)

        # "Lees CSV-bestand" knippert als een CSV-bestand is gevonden
        self.csv_button = tk.Button(root, text="Lees CSV-bestand", command=self.read_csv, bg=BUTTON_BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR)
        self.csv_button.grid(row=2, column=1, pady=10, sticky='n')
        self.blink_csv_button()

        # Knop voor help met link naar instructie.pdf
        tk.Button(root, text="?", command=self.open_help, bg=HELP_BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).grid(row=0, column=3, padx=10, pady=10)

        tk.Label(root, text="Selecteer kolommen voor het pad:", bg=APP_BACKGROUND_COLOR).grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.path_listbox = self.create_listbox_with_buttons(root, 4, 0)

        tk.Label(root, text="Selecteer kolommen voor de studentmap:", bg=APP_BACKGROUND_COLOR).grid(row=3, column=1, padx=10, pady=10, sticky='e')
        self.name_listbox = self.create_listbox_with_buttons(root, 4, 1)

        tk.Label(root, text="Selecteer kolommen voor de prefix van de bestanden:", bg=APP_BACKGROUND_COLOR).grid(row=3, column=2, padx=10, pady=10, sticky='e')
        self.prefix_listbox = self.create_listbox_with_buttons(root, 4, 2)

        tk.Button(root, text="Verplaats bestanden", command=self.move_files, bg=BUTTON_BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR).grid(row=5, column=1, pady=20)

        # Initialisatie van de attributen met de gegeven waarden
        if initial_csv_path:
            self.csv_file_path.set(initial_csv_path)

        if initial_source_folder:
            self.source_folder.set(initial_source_folder)

    def create_listbox_with_buttons(self, root, row, column):
        frame = tk.Frame(root, bg=FRAME_BACKGROUND_COLOR, bd=5, relief="ridge")  # Lichtgroen kader, ridge relief voor een 3D-effect
        frame.grid(row=row, column=column, padx=10, pady=10, sticky='nsew')

        listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, exportselection=0, bg='white')  # Witte achtergrondkleur
        listbox.pack(side=tk.LEFT, padx=5, fill=tk.BOTH)

        button_frame = tk.Frame(frame, bg=FRAME_BACKGROUND_COLOR)  # Lichtgroen kader
        button_frame.pack(side=tk.LEFT)

        up_button = tk.Button(button_frame, text="Omhoog", command=lambda lb=listbox: self.move_item_up(lb), bg=BUTTON_BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR)  # Willekeurige achtergrondkleur
        up_button.pack(side=tk.TOP, fill=tk.X)

        down_button = tk.Button(button_frame, text="Omlaag", command=lambda lb=listbox: self.move_item_down(lb), bg=BUTTON_BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR)  # Willekeurige achtergrondkleur
        down_button.pack(side=tk.TOP, fill=tk.X)

        return listbox

    def browse_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV-bestanden", "*.csv")])
        self.csv_file_path.set(file_path)
        return file_path

    def browse_source(self):
        folder_path = filedialog.askdirectory()
        self.source_folder.set(folder_path)
        return folder_path

    def read_csv(self):
        csv_file_path = self.csv_file_path.get()
        if not os.path.isfile(csv_file_path):
            messagebox.showerror("Fout", "Selecteer eerst een geldig CSV-bestand.")
            return None

        try:
            df = pd.read_csv(csv_file_path, sep=';', na_values=[''], keep_default_na=False)
        except Exception as e:
            messagebox.showerror("Fout", f"Fout bij het lezen van CSV-bestand:\n{e}")
            return None

        df = df.dropna(axis=1, how='all')

        self.update_listbox(self.path_listbox, df.columns)
        self.update_listbox(self.name_listbox, df.columns)
        self.update_listbox(self.prefix_listbox, df.columns)

        self.selected_path_columns = []
        self.selected_name_columns = []
        self.selected_prefix_columns = []

        return df

    def update_listbox(self, listbox, column_names):
        listbox.delete(0, tk.END)
        for name in column_names:
            listbox.insert(tk.END, name)

    def move_item_up(self, listbox):
        selected_indices = listbox.curselection()
        if selected_indices:
            for i in selected_indices:
                if i > 0:
                    # Verplaats het item omhoog in de lijst
                    text = listbox.get(i)
                    listbox.delete(i)
                    listbox.insert(i - 1, text)
                    listbox.selection_set(i - 1)

    def move_item_down(self, listbox):
        selected_indices = listbox.curselection()
        if selected_indices:
            for i in reversed(selected_indices):
                if i < listbox.size() - 1:
                    # Verplaats het item omlaag in de lijst
                    text = listbox.get(i)
                    listbox.delete(i)
                    listbox.insert(i + 1, text)
                    listbox.selection_set(i + 1)

    def move_files(self):
        csv_file_path = self.csv_file_path.get()
        source_folder = self.source_folder.get()
        destination_root = "C:/testdoel/"

        if not os.path.isfile(csv_file_path) or not os.path.isdir(source_folder):
            messagebox.showerror("Fout", "Ongeldige bestands- of maplocatie.")
            return

        try:
            df = pd.read_csv(csv_file_path, sep=';', na_values=[''], keep_default_na=False)
        except Exception as e:
            messagebox.showerror("Fout", f"Fout bij het lezen van CSV-bestand:\n{e}")
            return

        df = df.dropna(axis=1, how='all')

        path_indices = self.path_listbox.curselection()
        name_indices = self.name_listbox.curselection()
        prefix_indices = self.prefix_listbox.curselection()

        if not path_indices or not name_indices or not prefix_indices:
            messagebox.showerror("Fout", "Selecteer minstens één kolom voor het pad, de bestandsnaam en het prefix.")
            return

        self.selected_path_columns = [self.path_listbox.get(idx) for idx in path_indices]
        self.selected_name_columns = [self.name_listbox.get(idx) for idx in name_indices]
        self.selected_prefix_columns = [self.prefix_listbox.get(idx) for idx in prefix_indices]

        for _, row in df.iterrows():
            destination_path = os.path.join(destination_root, *[str(row[name]) for name in self.selected_path_columns])

            folder_name_parts = [str(row[name]) for name in self.selected_name_columns]
            folder_name = "_".join(folder_name_parts)

            prefix_parts = [str(row[name]) for name in self.selected_prefix_columns]
            file_prefix = "_".join(prefix_parts)

            destination_path = os.path.join(destination_path, folder_name)

            self.create_directory(destination_path)

            for filename in os.listdir(source_folder):
                source_file = os.path.join(source_folder, filename)

                file_name_parts = [str(row[name]) for name in self.selected_name_columns]
                new_file_name = file_prefix + "_" + os.path.splitext(filename)[0] + os.path.splitext(filename)[1]

                destination_file = os.path.join(destination_path, new_file_name)

                shutil.copy2(source_file, destination_file)

        messagebox.showinfo("Voltooid", "Bestanden zijn gekopieerd!")

    def create_directory(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except PermissionError:
            messagebox.showerror("Fout", f"Toegang geweigerd bij het maken van de map:\n{path}")
        except Exception as e:
            messagebox.showerror("Fout", f"Fout bij het maken van de map:\n{e}")

    def blink_csv_button(self):
        # Knippert de "Lees CSV-bestand" knop als een CSV-bestand is gevonden
        csv_file_path = self.csv_file_path.get()
        if os.path.isfile(csv_file_path):
            self.csv_button.config(bg=CSV_BUTTON_BLINK_COLOR)
            self.root.after(500, lambda: self.csv_button.config(bg=BUTTON_BACKGROUND_COLOR))
            self.root.after(1000, self.blink_csv_button)

    def open_help(self):
        # Open het helpvenster met instructies
        help_window = tk.Toplevel(self.root)
        help_window.title("Instructies")

        # Lees de instructies uit de PDF met PyMuPDF
        pdf_path = "instructies.pdf"  # Naam van het PDF-bestand
        if os.path.isfile(pdf_path):
            with fitz.open(pdf_path) as pdf_document:
                text = ""
                for page_number in range(pdf_document.page_count):
                    page = pdf_document.load_page(page_number)
                    text += page.get_text()

                # Toon de instructies in een label
                label = tk.Label(help_window, text=text, wraplength=600, justify=tk.LEFT)
                label.pack(padx=10, pady=10)
        else:
            label = tk.Label(help_window, text="Instructiebestand niet gevonden.", wraplength=600, justify=tk.LEFT)
            label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileMoverApp(root)
    root.mainloop()
