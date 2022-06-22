import tkinter as tk
from typing import Text

scherm=tk.Tk()

groet=tk.Label(
    text="hoi wereld",
    foreground="red",
    background="black",
    padx=50,
    pady=100
    )

invoerveld1=tk.Entry(
    bd =15
)

melding=tk.Label(text="MOOI weer vandaag.....de zon schijnt en er is geen regen",

  foreground="green",
    background="yellow",
    padx=50,
    pady=100
)

groet.pack()
invoerveld1.pack()
melding.pack()

scherm.mainloop()