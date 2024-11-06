# Event binding III (Keyboard)

import tkinter as tk
from tkinter import ttk

# Function to handle key press events
def key_press(event):
    # Update lbl2 with the key symbol of the pressed key
    lbl2["text"] = event.keysym

# Function to handle focus gained events
def focus_gained(event):
    # Update lbl2 with "Focus Gained" when the entry widget gains focus
    lbl2["text"] = "Focus Gained"

# Function to handle focus lost events
def focus_lost(event):
    # Update lbl2 with "Focus Lost" when the entry widget loses focus
    lbl2["text"] = "Focus Lost"
    
# Function to handle Return key press events
def return_key(event):
    # Update lbl2 with the uppercase text from the entry widget
    lbl2["text"] = entry.get().upper()
    
# Function to handle key combination events
def key_combination(event):
    # Update lbl2 with "Key combination triggered" when Control-A is pressed
    lbl2["text"] = "Key combination triggered"

win = tk.Tk()
win.title("Week 5")
win.geometry("400x250+500+200")
win.iconbitmap("python.ico")

# Create widgets
lbl1= ttk.Label(win, text="Enter your text and press <Return>")
entry = ttk.Entry(win, width=30)
btn = ttk.Button(win, text="Button")
lbl2 = ttk.Label(win, text="", font=("Consolas",12))

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
# Bind Control-A key combination in the main window to key_combination function
win.bind("<Control-a>", key_combination)

win.mainloop()