import tkinter as tk

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x300+100+100")

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="white")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

# side: Defines the side of the container where the widget is placed 
# (top, left, right, bottom)
label1.pack(ipadx=10, ipady=10, fill="y", side="top")
label2.pack(ipadx=10, ipady=10, fill="y", side="left")
label3.pack(ipadx=10, ipady=10, fill="y", side="right")

win.mainloop()
