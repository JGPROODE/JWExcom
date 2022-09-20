# Python program to create
# a file explorer in Tkinter
#import os
from fileinput import filename
import shutil
# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer window

filename=""

def browseFiles():
	global filename

	filename = filedialog.askopenfilename(initialdir = "\\",
										title = "Select a File",
										filetypes = (("all files",
														"*.*"),("Text files",
														"*.txt*")))
	
	# Change label contents
 	
	label_file_explorer.configure(text="File Opened: "+filename)
	print(filename)


padnaam=filename.split("/")
print(padnaam[-1])
bestandsnaam=padnaam[-1]
bronpad= "C:\\tmp\\25604bolbbl202020212022\\"  

def copyFile():
    shutil.copy(filename, "c:\\tmp\\"+bestandsnaam)
    	
																								
# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
							text = "File Explorer using Tkinter",
							width = 100, height = 4,
							fg = "blue")

	
button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

button_copy = Button(window,
					text = "Copy",
					command = copyFile)

button_exit = Button(window,
					text = "Exit",
					command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)
button_copy.grid(column=1,row=3)

button_exit.grid(column = 1,row = 4)

# Let the window wait for any events
window.mainloop()
