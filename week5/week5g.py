# Center window

import tkinter as tk
from window_utils import center_window

# Create the main window
win = tk.Tk()

# Get the screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Define the desired window size
window_width = 400
window_height = 300

# Place the window using the "center_window" function
# This function calculates the position to center the window on the screen
win.geometry(center_window(screen_width, screen_height, window_width, window_height))

# Set the window title and icon
win.title("Week 5")
win.iconbitmap("python.ico")

win.mainloop()
