import tkinter as tk

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x300+100+100")


# uniform: Creates groups of rows or columns that will resize uniformly. 
# It can take any string value of your choice.

# index: Specifies the column index (0, 1, 2).

# weight: Determines how much the column should expand relative to other columns. 
# Higher weight means more expansion.

# uniform: Ensures that all columns with the same uniform value resize uniformly. 
# Here, all columns have the same uniform value "eq".

win.columnconfigure(index=0, weight=1, uniform="eq")
win.columnconfigure(index=1, weight=2, uniform="eq")
win.columnconfigure(index=2, weight=3, uniform="eq")
win.rowconfigure(index=0, weight=1, uniform="eq")
win.rowconfigure(index=1, weight=1, uniform="eq")
win.rowconfigure(index=2, weight=1, uniform="eq")

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="white")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

# sticky: Controls widget alignment or stretching within the grid cell.
# rowspan / columnspan: Allows a widget to span multiple rows or columns.
label1.grid(row=0, column=0, sticky="nswe") # rowspan=2
label2.grid(row=1, column=2, sticky="nswe")
label3.grid(row=2, column=1, sticky="nswe") # columnspan=2

win.mainloop()