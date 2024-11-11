import tkinter as tk

win = tk.Tk()
win.title("Week 2")
win.geometry("300x300+100+100")
# normal (regular sized), zoomed (zoomed), iconic(shows up to pocket), withdrawn(no sight)
win.state(newstate="withdrawn")
win.mainloop()