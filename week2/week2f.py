import tkinter as tk

win = tk.Tk() # How can we create the main application window?
win.title("Week 2") # How can we set the window title?
win.iconbitmap("python.ico") # How can we add a custom icon to the window?
win.geometry("300x300+100+100") # How can we configure the window’s size and position?
#           ("Width x Height + x + y")
win.resizable(False, False) # How can we make the window non-resizable?

# How can we create labels in the window?
label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="#ffffff")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

# How can we display labels in the window?
label1.pack()
label2.pack()
label3.pack()

# How can we keep the application running?
win.mainloop()
