# Toplevel

import tkinter as tk
from tkinter import ttk

# Function to open a second window
def open_second_window():
    # Create a new top-level window (second window)
    win2 = tk.Toplevel(win)
    win2.title("Second Window")
    win2.geometry("300x200+550+250")
    
    # Uncomment the following line to make the second window modal
    # win2.grab_set()  # Restricts all user interactions to this window only (modal window).
    
    # Add a label to the second window
    ttk.Label(win2, text="Second Window").pack(pady=(20, 0))
    
    # Add a button to close the second window
    ttk.Button(win2, text="Close", command=win2.destroy).pack(pady=(20, 0))

# Create the main window
win = tk.Tk()
win.title("Week 6")
win.geometry("300x300+500+200")
win.iconbitmap("python.ico")

# Create buttons in the main window
btn1 = ttk.Button(win, text="Open Second Window", command=open_second_window)
btn2 = ttk.Button(win, text="Close", command=win.destroy)

# Pack the buttons into the main window
btn1.pack(pady=(20, 0))
btn2.pack(pady=(20, 0))

# Start the main loop to run the application
win.mainloop()