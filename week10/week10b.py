# Install customtkinter: pip install customtkinter
# Basic CTk GUI with classes

import customtkinter as ctk  # Importing customtkinter for custom GUI components

class CTkApp(ctk.CTk):  # Defining a class that inherits from ctk.CTk
    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.geometry("300x200")  # Setting the window size
        self.title("Week 10")  # Setting the window title
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop

    def create_widgets(self):  # Method to create widgets
        self.lbl = ctk.CTkLabel(self, text="GUI Programming with Python", fg_color=("orange", "green"), corner_radius=20)  # Creating a CTkLabel
        self.btn = ctk.CTkButton(self, text="Change Appearance", command=self.change_appearance)  # Creating a CTkButton

    def create_layout(self):  # Method to create layout
        self.lbl.pack(pady=20)  # Packing the label with padding
        self.btn.pack()  # Packing the button

    def change_appearance(self):  # Method to change appearance mode
        if ctk.get_appearance_mode() == "Dark":  # Checking if current mode is Dark
            ctk.set_appearance_mode("Light")  # Setting appearance mode to Light
        else:
            ctk.set_appearance_mode("Dark")  # Setting appearance mode to Dark

app = CTkApp()  # Creating an instance of CTkApp