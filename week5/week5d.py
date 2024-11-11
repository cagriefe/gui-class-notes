# Context menu

import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Function to show the context menu
def show_context_menu(event):
    # Places the context menu at the (x, y) coordinate of the mouse.
    # event.x_root, event.y_root returns the coordinate
    # of the mouse relative to the top left corner of the screen.
    # event.x, event.y returns the coordinate of the mouse relative 
    # to the top left corner of the widget.
    context_menu.post(event.x_root, event.y_root)
# Function to show the current date and time
def show_date():
    # Create a new label with the current date and time and add it to the list of labels
    labels.append(ttk.Label(win, text=datetime.now().strftime("%d.%m.%Y - %H:%M:%S"),
                            font=("Consolas", 16)))
    # Pack the new label into the window
    labels[-1].pack(pady=(10, 0))
# Function to clear all date and time labels
def clear():
    # Destroy each label in the list of labels
    for label in labels:
        label.destroy()
    # Clear the list of labels
    labels.clear()

# Create the main window
win = tk.Tk()
win.title("Week 5")
win.geometry("300x300+500+200")



labels = []
# Create the context menu
context_menu = tk.Menu(win, tearoff=False)
# Add commands to the context menu
context_menu.add_command(label="Show date and time", command=show_date)
context_menu.add_command(label="Clear", command=clear)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=win.destroy)
# Bind right mouse button click to show the context menu
win.bind("<Button-3>", show_context_menu)

# Start the main loop
win.mainloop()