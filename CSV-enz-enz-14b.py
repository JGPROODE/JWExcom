import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class FileMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bestandsverplaatsingstool")

        self.csv_file_path = tk.StringVar()
        self.source_folder = tk.StringVar()

        # Variables to store selected columns and their order
        self.selected_columns_sets = []  # List to store selected column sets
        self.column_orders = []  # List to store column orders for each set

        # Dictionary to store column_listbox widgets
        self.column_listboxes = {}

        tk.Label(root, text="Pad naar CSV-bestand:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.csv_file_path, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(root, text="Blader...", command=self.browse_csv).grid(row=0, column=2, padx=10, pady=10)

        tk.Label(root, text="Pad naar bronmap:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.source_folder, width=50).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(root, text="Blader...", command=self.browse_source).grid(row=1, column=2, padx=10, pady=10)

        tk.Button(root, text="Lees CSV-bestand", command=self.read_csv).grid(row=2, column=1, pady=10)

        for i in range(3, 12, 3):
            self.create_column_selection_widgets(root, i, f"Selecteer kolommen {i // 3 + 1}:")

        tk.Button(root, text="Verplaats bestanden", command=self.move_files).grid(row=12, column=1, pady=20)

    def create_column_selection_widgets(self, parent, row, label_text):
        tk.Label(parent, text=label_text).grid(row=row, column=0, padx=10, pady=10)
        column_listbox = tk.Listbox(parent, selectmode=tk.MULTIPLE, exportselection=0)
        column_listbox.grid(row=row + 1, column=0, padx=10, pady=10)
        tk.Button(parent, text=f"Selecteer kolomvolgorde {row // 3}", command=lambda cl=column_listbox: self.select_column_order(cl)).grid(row=row + 1, column=1, pady=10)

        # Store the column_listbox widget in the dictionary
        self.column_listboxes[row] = column_listbox

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
            df = pd.read_csv(csv_file_path, sep=';', na_values=[''], keep_default_na=False)
        except pd.errors.EmptyDataError:
            messagebox.showerror("Fout", "Het CSV-bestand is leeg.")
            return
        except Exception as e:
            messagebox.showerror("Fout", f"Fout bij het lezen van CSV-bestand:\n{e}")
            return

        df = df.dropna(axis=1, how='all')

        # Create and update column selection widgets
        for i in range(3, 12, 3):
            self.create_column_selection_widgets(self.root, i, f"Selecteer kolommen {i // 3 + 1}:")

            # Access the column_listbox widget from the dictionary
            column_listbox = self.column_listboxes.get(i)
            
            if column_listbox:
                # Update the listbox with column names
                self.update_listbox(column_listbox, df.columns)

        self.selected_columns_sets = []
        self.column_orders = []

    def select_column_order(self, column_listbox):
        selected_indices = column_listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Fout", "Selecteer minstens één kolom.")
            return

        # Get the selected columns in the order they were selected
        selected_columns = [column_listbox.get(idx) for idx in selected_indices]

        # Create a new window to display the selected columns and set their order
        order_window = tk.Toplevel(self.root)
        order_window.title("Kies kolomvolgorde")

        tk.Label(order_window, text="Selecteer de volgorde voor de geselecteerde kolommen:").pack(pady=10)

        # Listbox to display and set the order of selected columns
        order_listbox = tk.Listbox(order_window, selectmode=tk.MULTIPLE, exportselection=0)
        order_listbox.pack(pady=10)

        for column in selected_columns:
            order_listbox.insert(tk.END, column)

        # Function to set the order of selected columns
        def set_order():
            selected_order_indices = order_listbox.curselection()
            if not selected_order_indices or len(selected_order_indices) != len(selected_columns):
                messagebox.showerror("Fout", "Selecteer een geldige volgorde voor alle kolommen.")
                return

            # Get the selected order for the columns
            column_order = [selected_columns[idx] for idx in selected_order_indices]

            # Store the selected columns and their order
            self.selected_columns_sets.append(selected_columns)
            self.column_orders.append(column_order)

            order_window.destroy()

        # Button to set the order
        tk.Button(order_window, text="Set Order", command=set_order).pack(pady=10)

    def update_listbox(self, listbox, column_names):
        listbox.delete(0, tk.END)
        for name in column_names:
            listbox.insert(tk.END, name)

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

        if not self.selected_columns_sets:
            messagebox.showerror("Fout", "Selecteer eerst de kolomvolgorde.")
            return

        for set_index, (selected_columns, column_order) in enumerate(zip(self.selected_columns_sets, self.column_orders)):
            for _, row in df.iterrows():
                destination_path = os.path.join(destination_root, *[str(row[name]) for name in column_order])

                folder_name_parts = [str(row[name]) for name in column_order]
                folder_name = "_".join(folder_name_parts)

                destination_path = os.path.join(destination_path, folder_name)

                self.create_directory(destination_path)

                for filename in os.listdir(source_folder):
                    source_file = os.path.join(source_folder, filename)

                    new_file_name = "_".join([str(row[name]) for name in column_order]) + os.path.splitext(filename)[1]

                    destination_file = os.path.join(destination_path, new_file_name)

                    shutil.copy2(source_file, destination_file)

            messagebox.showinfo("Voltooid", f"Bestanden zijn gekopieerd voor kolomset {set_index + 1}!")

    def create_directory(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except PermissionError:
            messagebox.showerror("Fout", f"Toegang geweigerd bij het maken van de map:\n{path}")
        except Exception as e:
            messagebox.showerror("Fout", f"Fout bij het maken van de map:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileMoverApp(root)
    root.mainloop()
