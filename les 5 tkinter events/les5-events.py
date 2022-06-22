# Maak een of meerdere van onderstaande applicaties (easy, medium of hard) 
# die de leeftijd berekent aan de hand van een geboortejaar of geboortedatum.

#################################################################################################
# MEDIUM

import tkinter as tk
import student as st

window = tk.Tk() 
window.title('Bereken je leeftijd | Voor als je het even vergeten bent')


window.geometry("650x200")
window.configure(bg='#333')


### WIDGETS ###
# Create main label widget
label_main = tk.Label(window, text="Wat is je geboortedatum?",
    background = "#333",
    foreground ="lightblue",
    font = "Helvetica",
    pady = 20)

# Create label widget
label_jaar = tk.Label(window, text = "Jaar:", 
    background = "#333",
    foreground ="lightblue",
    font = "Helvetica")
label_maand = tk.Label(window, text = "Maand (1-12):", 
    background = "#333",
    foreground ="lightblue",
    font = "Helvetica")
label_dag = tk.Label(window, text = "Dag (1-31):", 
    background = "#333",
    foreground ="lightblue",
    font = "Helvetica")


# Create entry widgets
entry_jaar = tk.Entry(master=window, width=15,
    background = "white",
    foreground ="#333",
    font = "Helvetica",
    borderwidth=2, 
    relief="solid")
entry_maand = tk.Entry(master=window, width=15,
    background = "white",
    foreground ="#333",
    font = "Helvetica",
    borderwidth=2, 
    relief="solid")
entry_dag = tk.Entry(master=window, width=15,
    background = "white",
    foreground ="#333",
    font = "Helvetica",
    borderwidth=2, 
    relief="solid")

### BUTTONS ###
btn_submit = tk.Button(master=window, text="Verzend",
    background = "white",
    foreground ="#333") #submit button
btn_clear = tk.Button(master=window, text="Verwijder input",
    background = "white",
    foreground ="#333"  ) #clear button


# Create grid
label_main.grid(row=0, column=0, columnspan = 4, sticky= '' )
label_dag.grid(row=1, column=0,  sticky= 'w' )
label_maand.grid(row=1, column=1, sticky= 'w' )
label_jaar.grid(row=1, column=2, sticky= 'w' )
entry_dag.grid(row=2, column=0, sticky= '' )
entry_maand.grid(row=2, column=1, sticky= '' )
entry_jaar.grid(row=2, column=2, sticky= '' )
btn_submit.grid(row=2, column=3, sticky= 'e')
btn_clear.grid(row=3, column=3, sticky='e')

# Submit event handler
def handle_submit(event):
    try:
        student = st.Student(int(entry_dag.get()), int(entry_maand.get()), int(entry_jaar.get()))
        label_main["text"] = "Je bent nu " + str(student.bereken_leeftijd()) + " jaar oud."
    except:
        entry_jaar.delete(0, 'end')
        entry_maand.delete(0, 'end')
        entry_dag.delete(0, 'end')
        label_main["text"] = "Vul een geldige datum in!"

# Clear event handler
def handle_clear(event):
    entry_jaar.delete(0, 'end')
    entry_maand.delete(0, 'end')
    entry_dag.delete(0, 'end')

# Bind buttons with event handlers
btn_submit.bind("<Button-1>", handle_submit)
btn_clear.bind("<Button-1>", handle_clear)

window.mainloop() 
#################################################################################

# DROPDOWN MENU
# https://www.tutorialspoint.com/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter 





