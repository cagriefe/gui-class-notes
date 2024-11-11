# Center window

import tkinter as tk
from window_utils import center_window

def center_window(screen_width, screen_height, window_width, window_height):
    # Calculate the x coordinate for the window to be centered
    x = int((screen_width / 2) - (window_width / 2))
    
    # Calculate the y coordinate for the window to be centered
    y = int((screen_height / 2) - (window_height / 2))

    # Return the geometry string for the window
    # This string specifies the width, height, and position of the window
    return f"{window_width}x{window_height}+{x}+{y}"
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
