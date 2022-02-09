from tkinter import *
import tkinter as tk
from random import randint
import json
from tkinter import messagebox

# -------------------- Import JSON --------------------- #

try:
    with open('gods.json', 'r') as json_file:
        data = json.load(json_file)

    # -------------------- Clear Entry Text --------------------- #

    def click_on_entry_type_god_name(event):
        entry_type_god_name.configure(state = NORMAL)
        entry_type_god_name.delete(0, tk.END)
        entry_type_god_name.unbind('<Button-1>', clicked)

    # Put this after entry init
    # clicked = entry_type_god_name.bind('<Button-1>', click_on_entry_type_god_name)

    # -------------------- Buttons Functionality --------------------- #
    def clicked_button_random_god():
        # get value from dropdown menu
        god_class = tkvar.get()
        print(f'Selected class is: {god_class}')
        print()
        if god_class == 'Choose class':
            label_show_results.config(text = '\n\nPlease choose a class!')

        class_selected_gods_list = []
        # put gods from selected class in a list
        for key, value in data.items():
            if god_class.lower() == 'any':
                class_selected_gods_list.append(key)
            elif god_class.lower() in value['class']:
                class_selected_gods_list.append(key)

        random_list_position = randint(0, len(class_selected_gods_list)-1)
        chosen_god = class_selected_gods_list[random_list_position]
        random_skin_list_position = randint(0, len(data[chosen_god]['skins'])-1)
        chosen_skin = data[chosen_god]['skins'][random_skin_list_position]
        print(f'List of gods in {god_class} class : {class_selected_gods_list}')
        print(f'Number of gods in {god_class} class: {len(class_selected_gods_list)}')
        print(f'Random position in list: {random_list_position} (add one for the visual list)')
        print(f'Chosen god: {chosen_god}')
        print(f'Chosen skin: {chosen_skin}')
        print('--------------------')
        print()
        label_show_results.config(text=f'\n\n**********\nChosen god: {chosen_god} \nChosen skin: '
                                       f'{chosen_skin}\n***********')


    def clicked_button_random_skin():
        # get entry value
        god_name_or_nick = entry_type_god_name.get()
        chosen_god = ''
        print(f'Typed text: {god_name_or_nick}')
        print()
        for key, value in data.items():
            try:
                # if god_name_or_nick.upper() in value['nick']:
                if god_name_or_nick.lower() in value['nick'].lower():
                    chosen_god = key
            # if nick value does not exist move on
            except KeyError:
                pass

            # if god_name_or_nick.capitalize() in key:
            if god_name_or_nick.lower() in key.lower():
                if chosen_god != '':
                    pass
                else:
                    chosen_god = key

        if chosen_god != '':
            random_skin_list_position = randint(0, len(data[chosen_god]['skins']) - 1)
            chosen_skin = data[chosen_god]['skins'][random_skin_list_position]
            print(f'Chosen god: {chosen_god}')
            print(f'Chosen skin: {chosen_skin}')
            print('--------------------')

            label_show_results.config(text = f'\n\n**********\nChosen god: {chosen_god} \nChosen skin: '
                                             f'{chosen_skin}\n**********')
        else:
            print('You do not have this god or you typed wrong. Please try again!')
            label_show_results.config(text = f'\n\nYou do not have {god_name_or_nick} god \nor you typed wrong. \nPlease '
                                             f'try again!')
        print()

    # -------------------- UI Setup --------------------- #

    window = tk.Tk()
    window.title('Smite randomizer')
    window.config(padx = 35, pady = 35)

    # creating tkinter var for retaining dropdown menu options
    tkvar = StringVar(window)

    # dropdown menu list of choices and initial value
    hero_class = {'Any', 'Assassin', 'Guardian', 'Hunter', 'Mage', 'Warrior'}
    tkvar.set('Choose class')

    # dropdown menu
    dropdown_menu = tk.OptionMenu(window, tkvar, *hero_class)
    dropdown_menu.grid(row = 2, column = 1)
    dropdown_menu.config(width = 13)

    # entry init + options
    entry_type_god_name = tk.Entry(width = 18)
    entry_type_god_name.grid(row = 2, column = 2)
    entry_type_god_name.insert(0, 'God name or nick')
    # entry binding for clearing value on click. Works with click_on_entry_type_god_name function
    clicked = entry_type_god_name.bind('<Button-1>', click_on_entry_type_god_name)

    # buttons init
    button_random_god = tk.Button(text = 'Random god', command = clicked_button_random_god, width = 15)
    button_random_skin = tk.Button(text = 'Random skin', command = clicked_button_random_skin, width = 15)

    # buttons grid position
    button_random_god.grid(row = 3, column = 1)
    button_random_skin.grid(row = 3, column = 2)

    # result label init and options
    label_show_results = tk.Label(text = '\n\n**********\n\n**********')
    label_show_results.grid(row = 5, column = 1, columnspan = 2, rowspan = 4)

    # -------------------- Tracing of dropdown menu value -------------------- #
    # function needed because trace can't work without a callback function. The function can be left empty (pass)
    def change_dropdown(*args):
        print(tkvar.get())
        print()
        # pass

    # trace change of tkvar value in dropdown menu
    tkvar.trace('w', change_dropdown)

    tk.mainloop()

except FileNotFoundError:
    messagebox.showinfo(title = 'File not found!', message = 'File gods.json not found. Please make sure you have the file in the same folder and restart the program!')
