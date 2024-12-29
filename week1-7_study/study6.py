import tkinter as tk
from tkinter import ttk


def center_window(screen_width, screen_height,window_width, window_height):
    
    x = int((screen_width/2)-(window_width/2))
    y = int((screen_height/2)-(window_height/2))
    
    return(f"{window_width}x{window_height}+{x}+{y}")

win = tk.Tk()
win.title("Study 6")

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

window_width = 400
window_height = 200

win.geometry(center_window(screen_width, screen_height,window_width, window_height))

win.mainloop()