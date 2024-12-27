# Unit Converter

import customtkinter as ctk  # Importing customtkinter for custom GUI components

class UnitConverter(ctk.CTk):  # Defining a class that inherits from ctk.CTk
    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        ctk.set_default_color_theme("blue")  # Setting the default color theme to blue
        ctk.set_appearance_mode("light")  # Setting the appearance mode to light
        self.geometry("310x200")  # Setting the window size
        self.resizable(False, False)  # Disabling window resizing
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop
        
    def create_widgets(self):  # Method to create widgets
        self.container = ctk.CTkFrame(self)  # Creating a CTkFrame
        self.entry_label = ctk.CTkLabel(self.container, text="Enter Value:")  # Creating a label for the entry
        self.entry = ctk.CTkEntry(self.container)  # Creating an entry widget
        self.combo_label = ctk.CTkLabel(self.container, text="Convert:")  # Creating a label for the combobox
        self.unit_combobox = ctk.CTkOptionMenu(self.container, values=["Miles to Kilometers", "Kilometers to Miles"])  # Creating a combobox for unit selection
        self.convert_button = ctk.CTkButton(self.container, text="Convert", width=80, command=self.convert)  # Creating a button to trigger conversion
        self.result_label = ctk.CTkLabel(self.container, text="Enter a number and click the Convert button.")  # Creating a label to display the result
        
        self.bind("<Return>", lambda e : self.convert())  # Binding the Return key to the convert method
        
    def create_layout(self):  # Method to create layout
        self.container.pack(pady=10, padx=10, fill="both", expand=True)  # Packing the container with padding
        
        self.container.columnconfigure(index=0, weight=1)  # Configuring column 0
        self.container.columnconfigure(index=1, weight=2)  # Configuring column 1
        self.container.rowconfigure(index=0, weight=1)  # Configuring row 0
        self.container.rowconfigure(index=1, weight=1)  # Configuring row 1
        self.container.rowconfigure(index=2, weight=1)  # Configuring row 2
        self.container.rowconfigure(index=3, weight=1)  # Configuring row 3
        
        self.entry_label.grid(row=0, column=0, padx=10, pady=(10, 0))  # Placing the entry label in the grid
        self.entry.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="we")  # Placing the entry in the grid
        self.combo_label.grid(row=1, column=0, padx=10, pady=(10, 0))  # Placing the combobox label in the grid
        self.unit_combobox.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="we")  # Placing the combobox in the grid
        self.convert_button.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="e")  # Placing the convert button in the grid
        self.result_label.grid(row=3, column=0, padx=10, pady=(10, 0), columnspan=2)  # Placing the result label in the grid
        
    def convert(self):  # Method to perform conversion
        try:
            value = float(self.entry.get())  # Getting the value from the entry and converting it to float
            if self.unit_combobox.get() == "Miles to Kilometers":  # Checking if the conversion is from Miles to Kilometers
                result = value * 1.60934  # Converting Miles to Kilometers
                self.result_label.configure(text=f"{result:.2f} Kilometers")  # Updating the result label with the conversion result
            elif self.unit_combobox.get() == "Kilometers to Miles":  # Checking if the conversion is from Kilometers to Miles
                result = value / 1.60934  # Converting Kilometers to Miles
                self.result_label.configure(text=f"{result:.2f} Miles")  # Updating the result label with the conversion result
        
        except ValueError:  # Handling invalid input
            self.result_label.configure(text="Invalid Input!")  # Updating the result label with an error message
            
app = UnitConverter()  # Creating an instance of UnitConverter