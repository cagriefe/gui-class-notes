import tkinter as tk
from tkinter import ttk


# This function reads the input value, converts it based on the selected unit, 
# and updates the result label. If the input is not a valid number, 
# it displays an error message.
def convert():
    try:
        value = float(entry.get())
        if unit_combobox.get() == "Miles to Kilometers":
            result = value * 1.60934
            result_label.configure(text=f"{result:.2f} Kilometers")
        elif unit_combobox.get() == "Kilometers to Miles":
            result = value / 1.60934
            result_label.configure(text=f"{result:.2f} Miles")
    except ValueError:
        result_label.configure(text="Invalid input!")

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")
# win.resizable(width=False, height=False)

# A labeled frame to contain all widgets, with padding for better spacing.
container = ttk.LabelFrame(win, text="Unit Converter", padding="10")
container.pack(padx=15, pady=15, fill="both", expand=True)

# Configures the grid layout within the container, 
# setting weights for columns and rows to manage resizing behavior.
container.columnconfigure(index=0, weight=1)
container.columnconfigure(index=1, weight=2)
container.rowconfigure(index=0, weight=1)
container.rowconfigure(index=1, weight=1)
container.rowconfigure(index=2, weight=1)
container.rowconfigure(index=3, weight=1)

# Label and entry widget for user input.
entry_label = ttk.Label(container, text="Enter Value:")
entry_label.grid(row=0, column=0, padx=5, pady=5)
entry = ttk.Entry(container)
entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

# Label and combo box for selecting the conversion type. 
# The combo box is set to "Miles to Kilometers" by default.
combo_label = ttk.Label(container, text="Convert:")
combo_label.grid(row=1, column=0, padx=5, pady=5)
unit_combobox = ttk.Combobox(container, values=["Miles to Kilometers",
                                                "Kilometers to Miles"], state="readonly")
unit_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="we")
unit_combobox.set("Miles to Kilometers") # Default Value

# Button that triggers the convert function.
convert_button = ttk.Button(container, text="Convert", command=convert)
convert_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

# Label to display the conversion result.
result_label = ttk.Label(container, text="")
result_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

win.mainloop()
