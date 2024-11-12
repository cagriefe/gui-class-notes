import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        if combo_box.get() == "Product":
            result = value1 * value2
            result_answer.configure(text= f"{result}")
        elif combo_box.get() == "Sum":
            result = value1 + value2
            result_answer.configure(text= f"{result}")
        elif combo_box.get() == "Divide":
            if not value2 == 0:
                result = value1 / value2
            result_answer.configure(text= f"{result}")
        elif combo_box.get() == "Extract":
            result = value1 - value2
            result_answer.configure(text= f"{result}")
    except ValueError:
        result_answer.configure(text="Invalid input")  
  
win = tk.Tk()
win.title("Study")
win.geometry("500x500+400+200")
win.resizable(False,False)

win.columnconfigure(index=0, weight=1, uniform="eq")
win.columnconfigure(index=1, weight=1, uniform="eq")
win.columnconfigure(index=2, weight=1, uniform="eq")
win.rowconfigure(index=0, weight=1, uniform="eq" )
win.rowconfigure(index=1, weight=1, uniform="eq" )
win.rowconfigure(index=2, weight=1, uniform="eq" )
win.rowconfigure(index=3, weight=1, uniform="eq")
win.rowconfigure(index=4, weight=3, uniform="eq")

label1 = tk.Label(win, text="Calculator", fg="White")
label1.grid(row=0, column=0, columnspan=3)

entry1_label = tk.Label(win, text="First Number", fg="Red")
entry1 = tk.Entry(win)
entry2_label = tk.Label(win, text="Second Number", fg="Red")
entry2 = tk.Entry(win)
entry1_label.grid(row=1, column=0)
entry1.grid(row=2, column=0)
entry2_label.grid(row=1, column=1)
entry2.grid(row=2, column=1)

result_label = tk.Label(win, text="Result", fg="red")
result_answer = tk.Label(win, text="", fg="green")
result_label.grid(row=1, column=2)
result_answer.grid(row=2, column=2)

combo_box_label= tk.Label(win, text="Select:")
combo_box = ttk.Combobox(win, values = ["Product",
                                       "Sum",
                                       "Divide",
                                       "Extract"
                                       ], state ="readonly")
combo_box_label.grid(row=3, column=0)
combo_box.grid(row=3, column=1)



button = tk.Button(win, text="Product", fg="red", command=calculate)
button.grid(row=4, column=0, columnspan=3)

win.mainloop()

