import os
#from PIL import Image, ImageTk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from configparser import ConfigParser
#import requests


# FUNCTIE OM FOTO TOETEVOEGEN
def show_png():
    img = ImageTk.PhotoImage(file='C:\Python38\P2-3\png openen\02n.png')
    Label_1['image'] = img


# TKINTER SCREEN
root = Tk()

Label_1 = Label(root, image = '')

root.mainloop()


# FUNCTIE AANROEPEN OM FOTO TOETEVOEGEN
show_png()
