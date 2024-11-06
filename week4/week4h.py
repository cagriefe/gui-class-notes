# Spinbox

import tkinter as tk
from tkinter import ttk

# Function to handle the click event of the Spinbox
def click_handler():
    ttk.Label(win, text=spin_value.get()).pack()

win = tk.Tk()
win.title("Week 4")
win.geometry("300x800+400+100")
win.iconbitmap("python.ico")

# Variable to store the value of the Spinbox
spin_value = tk.StringVar()

# Tuple of values for the Spinbox
spin_values = tuple(str(i) for i in range(1, 20, 3))

# Creates a Spinbox with the specified values, wraps around the values, 
# binds it to the spin_value variable, and sets the command to click_handler.
spinbox1 = ttk.Spinbox(win, values=spin_values, wrap=True, textvariable=spin_value, command=click_handler)
# wrap: True makes the Spinbox cycle through the values.
# spinbox1 = ttk.Spinbox(win, from_=0, to=10, wrap=True, state="readonly", textvariable=spin_value)
# spinbox1 = ttk.Spinbox(win, values=("1", "3", "5", "7"), wrap=True, textvariable=spin_value)
# spinbox1 = ttk.Spinbox(win, values=spin_values, wrap=True, textvariable=spin_value)


# Packs the Spinbox into the window
spinbox1.pack()

win.mainloop()