import tkinter as tk
from tkinter import ttk

# button_handler: Updates label1's text with the 
# values from entry1, combo1, and the selected radio button.
def button_handler():
    label1.configure(text=entry1.get()+ " " 
                     + selected_combo_item.get()+ " " +selected_radio_item.get( ))

# checkbox_handler: Enables or disables button1 based on the state of checkbox1.
def checkbox_handler():
    if checkbox_state.get() == "Enabled":
        button1.configure(state="normal")
        label1.configure(text="Button enabled.")
    else:
        button1.configure(state="disabled")
        label1.configure(text="Button disabled.")

win = tk.Tk()
win.title("Week 3")
win.iconbitmap("python.ico")
win.geometry("300x330+100+100")

selected_combo_item = tk.StringVar(value="Option 2") #  Holds the selected value of the combo box.
selected_radio_item = tk.StringVar() # Holds the selected value of the radio buttons.
checkbox_state= tk.StringVar(value="Enabled") # Holds the state of the checkbox.

frame1 = ttk.LabelFrame(win, text="Some GUI Widgets") # A labeled frame to contain other widgets.
label1 = ttk.Label(win, text="Label") # A label to display text.
entry1 = ttk.Entry(frame1, width=30) # An entry widget for text input.
# A combo box with two options, initially set to "Option 2".
combo1 = ttk.Combobox(frame1, width=15, textvariable=selected_combo_item, state="readonly") 
combo1["values"] = ("Option 1", "Option 2")
# Two radio buttons with values "A" and "B".
radio1 = ttk.Radiobutton(frame1, text="Item 1", value="A", variable="selected_radio_item")
radio2 = ttk.Radiobutton(frame1, text="Item 1", value="B", variable="selected_radio_item")
# A checkbox to enable or disable button1.
checkbox1 = ttk.Checkbutton(frame1, text="Enable Button", onvalue="Enabled", offvalue="Disabled",
                            variable=checkbox_state, command=checkbox_handler)
# A button that triggers button_handler.
button1 = ttk.Button(frame1, text="Send", command=button_handler) # state="disabled" (normal, disabled, active)

# pack method is used to place the widgets in the window with padding for better spacing.
frame1.pack(fill="both", expand=True, padx=10, pady=10)
label1.pack(pady=10)
entry1.pack(pady=10)
combo1.pack(pady=10)
radio1.pack(pady=10)
radio2.pack(pady=10)
checkbox1.pack(pady=10)
button1.pack(pady=10)

win.mainloop()