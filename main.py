from tkinter import *
import tkinter as tk
from tkinter import messagebox
from random import randint
import json



# -------------------- Buttons Functionality --------------------- #
def clicked_button_random_god():
    pass

def clicked_button_random_skin():
    pass

# -------------------- UI Setup --------------------- #

window = tk.Tk()
window.title('Smite randomizer')
window.config(padx=35, pady=35)

# creating tkinter var for retaining dropdown menu options
tkvar = StringVar(window)

# dropdown menu list of choices and initial value
hero_class = {'Any', 'Assassin', 'Guardian', 'Hunter', 'Mage', 'Warrior'}
tkvar.set('Choose class')

# dropdown menu
dropdown_menu = tk.OptionMenu(window, tkvar, *hero_class)
dropdown_menu.grid(row=2, column=1)
dropdown_menu.config(width=13)

# entry init + options
entry_type_god_name = tk.Entry(width=18)
entry_type_god_name.grid(row=2, column=2)
entry_type_god_name.insert(0, 'God name or nick')


# buttons init
button_random_god = tk.Button(text='Random god', command=clicked_button_random_god, width=15)
button_random_skin = tk.Button(text='Random skin', command=clicked_button_random_skin, width=15)

# buttons grid position
button_random_god.grid(row=3, column=1)
button_random_skin.grid(row=3, column=2)

# result label init and options
label_show_results = tk.Label(text='\n\n**********\n\n**********')
label_show_results.grid(row=5, column=1, columnspan=2, rowspan=4)



tk.mainloop()