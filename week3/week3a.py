import tkinter as tk

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x300+200+100")

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="green", fg="#ffffff")
label3 = tk.Label(win, text="Label 3", bg="blue", fg="white")

# How can we position labels at 
# specific coordinates in the window?
label1.place(x=-0, y=0)
label2.place(x=200, y=230)
label3.place(x=20, y=120)

win.mainloop()