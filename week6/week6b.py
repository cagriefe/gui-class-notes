# Toplevel (show-hide main)

import tkinter as tk
from tkinter import ttk


# Create the main window
win = tk.Tk()
win.title("Week 6")
win.geometry("300x300+500+200")
win.iconbitmap("python.ico")

# Function to open the second window
def open_second_window():
    # Hide the main window
    win.withdraw()
    # Create a new top-level window (second window)
    global win2
    win2 = tk.Toplevel(win)
    win2.title("Second Window")
    win2.geometry("300x200+550+250")
    # Add a label to the second window
    ttk.Label(win2, text="Second Window").pack(pady=(20, 0))
    # Add a button to close the second window
    ttk.Button(win2, text="Close", command=close_second_window).pack(pady=(20, 0))
    # Handle the window close event (clicking the 'X' button)
    win2.protocol("WM_DELETE_WINDOW", close_second_window)
# Function to close the second window and show the main window
def close_second_window():
    # Show the main window
    win.deiconify()
    # Destroy the second window
    win2.destroy()
# Create buttons in the main window
btn1 = ttk.Button(win, text="Open Second Window", command=open_second_window)
btn2 = ttk.Button(win, text="Close", command=win.destroy)
# Pack the buttons into the main window
btn1.pack(pady=(20, 0))
btn2.pack(pady=(20, 0))


# Start the main loop to run the application
win.mainloop()