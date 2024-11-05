import tkinter as tk
from tkinter import ttk # is imported for themed widgets.
from tkinter.scrolledtext import ScrolledText # is imported for a text widget with a scrollbar.

def button_handler():
    win.destroy()

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x300+100+100")

notebook1 = ttk.Notebook(win) # A notebook widget to create tabs.
notebook1.pack(pady=20) # Adds padding around the notebook for better spacing.

# tab1 and tab2: Frames that will be used as tabs in the notebook.
tab1 = ttk.Frame(notebook1)
tab2 = ttk.Frame(notebook1)

tab1.pack()
tab2.pack()

notebook1.add(tab1, text="Tab 1") # Adds tab1 to the notebook with the label "Tab 1".
notebook1.add(tab2, text="Tab 2") # Adds tab2 to the notebook with the label "Tab 2".

#A scrolled text widget in tab1 with a width of 30 characters and a height of 10 lines.
# The text wraps at word boundaries. (none, char,  word)
scrolled_text1 = ScrolledText(tab1, width=30, height=10, wrap="word") 
# Makes the scrolled text widget expand to fill the available space in tab1.
scrolled_text1.pack(fill="both")


label1 = ttk.Label(tab2, text="This is tab 2.") # A label in tab2 with the text "This is tab 2."
button1 = ttk.Button(tab2, text="Exit", command=button_handler) # A button in tab2 that triggers button_handler to close the window.
label1.pack(pady=50)
button1.pack(pady=10)

win.mainloop()