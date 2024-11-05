import tkinter as tk
import random

# How can we create a function to handle button clicks?
def click_handler():
    random_number = random.randint(1,100)
    label1.configure(foreground="red")
    label1.configure(text=f"Random number: {random_number}")
    
win = tk.Tk() # How can we create the main application window?
win.title("Week 2") # How can we set the window title?
win.iconbitmap("python.ico") # How can we add a custom icon to the window?
win.geometry("300x300+100+100") # How can we configure the window’s size and position?

label1 = tk.Label(win, text="Click the button to generate a number!")
label1.pack()

# How can we create a button that triggers the click handler?
button1 = tk.Button(win, text="Generate Random Number", command=click_handler)
button1.pack()

win.mainloop()