import tkinter as tk

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x300+100+100")

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="white")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

# The grid() method organizes widgets in a grid structure with rows and columns.
# It allows for precise control over the placement of each widget.

label1.grid(row=0, column=0)
label2.grid(row=1, column=2)
label3.grid(row=2, column=1)

win.mainloop()