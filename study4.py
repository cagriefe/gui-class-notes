import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

def show_date():
    labels.append(ttk.Label(win, text=datetime.now().strftime("%d.%m.%Y - %H:%M:%S"), font=("Consolas", 16)))
    labels[-1].pack(pady=(10,0))

def clear():
    for label in labels:
        label.destroy()
    labels.clear()

win = tk.Tk()
win.title("Study 4")
win.geometry("500x500+300+200")

labels = []
context_menu = tk.Menu(win, tearoff=False)
context_menu.add_command(label="Show date and time", command=show_date)
context_menu.add_command(label="Clear", command=clear)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=win.destroy)

win.bind("<Button-2>", show_context_menu)

win.mainloop()