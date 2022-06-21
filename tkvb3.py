import tkinter as tk
from typing import Text

scherm=tk.Tk()

groet=tk.Label(text="hoi wereld")
melding=tk.Label(text="MOOI weer vandaag.....de zon schijnt en er is geen regen")

groet.pack()
melding.pack()

scherm.mainloop()