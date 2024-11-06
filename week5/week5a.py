# Event binding I (Mouse click)

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
    message = f"Clicked at: {event.x}, {event.y}.\n" # The coordinates of the click within the widget
    message += f"Screen coordinates: {event.x_root}, {event.y_root}.\n" # The screen coordinates of the click
    message += f"Event type: {event.type.name}.\n"
    message += f"Clicked button: {button_name}.\n"
    message += f"Button text: {event.widget["text"]}.\n"
    # Update the label with the event details
    lbl.configure(text=message)

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
# Button, Button-1, Button-2, Button-3, Double-Button, Double-Button-1, ButtonRelease, ButtonRelease-1, ...
btn_a.bind("<Button>", click_event)
btn_b.bind("<ButtonRelease-1>", click_event)

# Set focus to btn_a
btn_a.focus()

win.mainloop()
