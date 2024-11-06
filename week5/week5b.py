# Event binding II (Mouse move)

import tkinter as tk
from tkinter import ttk

# Function to handle mouse click events
def click_event(event):
    # Determine which mouse button was clicked
    button_name = "Unknown"
    if event.num == 1:
        button_name = "Left"
    elif event.num == 2:
        button_name = "Middle"
    elif event.num == 3:
        button_name = "Right"

    # Create a message with event details
    message = f"Clicked at: {event.x}, {event.y}.\n"
    message += f"Screen coordinates: {event.x_root}, {event.y_root}.\n"
    message += f"Event type: {event.type.name}.\n"
    message += f"Clicked button: {button_name}.\n"
    message += f"Button text: {event.widget["text"]}.\n"
    # Update the label with the event details
    lbl.configure(text=message)

# Function to handle mouse enter events
def mouse_enter(event):
    # event.widget["text"] = "Mouse entered"
    event.widget.configure(text="Mouse entered")

# Function to handle mouse leave events
def mouse_leave(event):
    event.widget["text"] = "Mouse left"

# Function to handle mouse move events
def mouse_move(event):
    win.title(f"{event.x}, {event.y}")

win = tk.Tk()
win.title("Week 5")
win.geometry("400x250+500+200")
win.iconbitmap("python.ico")

# Create two buttons and a label
btn_a = ttk.Button(win, text="Button A")
btn_b = ttk.Button(win, text="Button B")
lbl = ttk.Label(win, justify="center")

# Pack the buttons and label into the window
btn_a.pack(pady=(20, 0))
btn_b.pack(pady=20)
lbl.pack()

# Bind mouse click events to the buttons
# <Button-1>: Left mouse button click
# <Button-3>: Right mouse button click
btn_a.bind("<Button-1>", click_event)
btn_b.bind("<Button-3>", click_event)

# Bind mouse enter and leave events to btn_a
# <Enter>: Mouse enters the widget
# <Leave>: Mouse leaves the widget
btn_a.bind("<Enter>", mouse_enter)
btn_a.bind("<Leave>", mouse_leave)

# Bind mouse move events to the window
# <Motion>: Mouse moves within the window
win.bind("<Motion>", mouse_move)

# Set focus to btn_a
btn_a.focus()

win.mainloop()
