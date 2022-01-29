# groceryCalcGUI.py

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('300x220')
root.resizable(True, True)
root.title('Grocery Calculator')

e_weight = tk.Entry(root)
e_weight.pack(fill='x', padx=5, pady=5)
# pack() x = fill horiz, y = fill vert, side sets side it packs to (top, bot, lt, rt)

def lbs_kg(weight):
    libs = float(weight)
    kilos = libs * 0.453592
    return kilos

def kg_lbs(weight):
    kilos = float(weight)
    libs = kilos * 2.20462
    return libs

def show_weightconv():
    selection = selected_weight.get()
    s_weight = float(e_weight.get())
    if selection == 'Lb':
        w2 = ' Kg'
        conv = lbs_kg(s_weight)
    elif selection == 'Kg':
        w2 = ' Lb'
        conv = lbs_kg(s_weight)
    else:
        showinfo(title='ERROR', 
                message='You need to select a conversion')

    w_display = ttk.Label(text = str(s_weight) + " " + selection + " converts to: " + str(conv) + w2)
    w_display.pack(fill='x', padx=5, pady=5)
    

selected_weight = tk.StringVar()
weighttype = (('Kilograms', 'Kg'),
        ('Pounds UK', 'Lb'))

# label
label = ttk.Label(text="Select weight to convert from.")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for weight in weighttype:
    r = ttk.Radiobutton(
        root,
        text=weight[0],
        value=weight[1],
        variable=selected_weight)
    r.pack(fill='x', padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Convert Weight",
    command=show_weightconv)
button.pack(fill='x', padx=5, pady=5)

root.mainloop()