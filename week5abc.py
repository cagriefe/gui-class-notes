import tkinter as tk
from tkinter import ttk

# Function to handle mouse click events
def click_event(event):
    # Determine which mouse button was clicked
    if event.num == 1:
        lbl["text"] = "Left mouse button clicked"
    elif event.num == 3:
        lbl["text"] = "Right mouse button clicked"
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
# Function to handle key press events
def key_press(event):
    # Update lbl2 with the key symbol of the pressed key
    lbl2["text"] = event.keysym
# Function to handle focus gained events
def focus_gained(event):
    # Update lbl2 with "text" when the entry widget gains focus
    lbl2["text"] = "Focus Gained"
# Function to handle focus lost events
def focus_lost(event):
    # Update lbl2 with "text" when the entry widget loses focus
    lbl2["text"] = "Focus Lost"
# Function to handle Return key press events
def return_key(event):
    # Update lbl2 with the uppercase text from the entry widget
    lbl2["text"] = entry.get().upper()
# Function to handle key combination events
def key_combination(event):
    # Update lbl2 with "text" when Control-A is pressed
    lbl2["text"] = "Key combination triggered"


# Create the main window
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
# Create widgets for the second part
lbl1 = ttk.Label(win, text="Enter your text and press <Return>")
entry = ttk.Entry(win, width=30)
btn = ttk.Button(win, text="Button")
lbl2 = ttk.Label(win, text="", font=("Consolas", 12))
# Pack widgets into the window
lbl1.pack(pady=20)
entry.pack(pady=(0, 20))
btn.pack(pady=(0, 20))
lbl2.pack()
# Bind events to widgets
# Bind left mouse button click on the button to return_key function
btn.bind("<Button-1>", return_key)
# Bind any key press in the entry widget to key_press function
entry.bind("<Key>", key_press)
# Bind focus gain in the entry widget to focus_gained function
entry.bind("<FocusIn>", focus_gained)
# Bind focus loss in the entry widget to focus_lost function
entry.bind("<FocusOut>", focus_lost)
# Bind Return key press in the entry widget to return_key function
entry.bind("<Return>", return_key)
# Bind Control-A key combination in the main window to function
win.bind("<Control-a>", key_combination)

# Start the main loop
win.mainloop()