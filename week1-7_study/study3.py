import tkinter as tk
from tkinter import ttk


def click_event(event):
    if event.num == 1:
        lbl["text"] = "Left mouse button clicked"
    elif event.num == 2:
        lbl["text"] = "Right mouse button clicked"
    message = f"Clicked at: {event.x}, {event.y}.\n"
    message += f"Screen coordinates: {event.x_root}, {event.y_root}"
    lbl["text"] = message

win = tk.Tk()
win.title("Study 3")
win.geometry("500x500+300+200")

btn_a = ttk.Button(win, text="Button A")
btn_b = ttk.Button(win, text="Button B")
lbl = ttk.Label(win, justify="center")

btn_a.pack(pady=(20,0))
btn_b.pack(pady=20)
lbl.pack()

btn_a.bind("<Button-1>", click_event)
btn_b.bind("<Button-2>", click_event)


win.mainloop()