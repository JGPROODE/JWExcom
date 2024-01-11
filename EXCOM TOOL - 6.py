import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from PyPDF2 import PdfWriter

class FileMoverApp:
    def __init__(self, root, app_bg_color='#FF0000', title_bar_bg_color='#FFFF00', initial_csv_path=None, initial_source_folder=None):
        self.root = root
        self.root.title("J.G.P. Roode: \"Lees CSV, Maak Doelpad, Prefix voor mapnaam en verplaats de bestanden uit de BronMap-tool\" ")

        # Achtergrondkleur van de hele app
        self.root.configure(bg=app_bg_color)

        # Gele achtergrond met rode letters voor de titelbalk
        self.root.option_add('*TFrame*background', title_bar_bg_color)
        self.root.option_add('*TFrame*foreground', '#FF0000')  # Rood

        self.csv_file_path = tk.StringVar()
        self.source_folder = tk.StringVar()

        self.selected_path_columns = []
        self.selected_name_columns = []
        self.selected_prefix_columns = []

        # Rest van de code blijft hetzelfde

        # Initialisatie van de attributen met de gegeven waarden
        if initial_csv_path:
            self.csv_file_path.set(initial_csv_path)

        if initial_source_folder:
            self.source_folder.set(initial_source_folder)

if __name__ == "__main__":
    root = tk.Tk()
    app_bg_color = '#FF0000'  # Knalrood
    title_bar_bg_color = '#FFFF00'  # Geel
    app = FileMoverApp(root, app_bg_color=app_bg_color, title_bar_bg_color=title_bar_bg_color)
    root.mainloop()
