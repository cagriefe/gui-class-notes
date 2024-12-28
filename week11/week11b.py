# Basic ttkbootstrap GUI with classes

import ttkbootstrap as ttk  # Importing ttkbootstrap for themed tkinter widgets

class GUIApp(ttk.Window):  # Defining a class that inherits from ttk.Window
    def __init__(self):  # Constructor method
        super().__init__(themename="superhero")  # Calling the constructor of the parent class with a theme
        self.geometry("500x500")  # Setting the window size
        self.title("Week 11")  # Setting the window title
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop
        
    def create_widgets(self):  # Method to create widgets
        self.btn1 = ttk.Button(self, text="Button 1", bootstyle="success")  # Creating a button with "success" style
        self.btn2 = ttk.Button(self, text="Button 2", bootstyle=("info", "outline"))  # Creating a button with "info" and "outline" styles
        self.cbtn1 = ttk.Checkbutton(self, text="Check Button", bootstyle="warning-round-toggle")  # Creating a checkbutton with "warning-round-toggle" style
        self.date_entry = ttk.DateEntry(self, bootstyle="success", width=10)  # Creating a date entry with "success" style
        
    def create_layout(self):  # Method to create layout
        self.btn1.pack(padx=15, pady=(30,15))  # Packing the first button with padding
        self.btn2.pack(padx=15, pady=15)  # Packing the second button with padding
        self.cbtn1.pack(padx=15, pady=15)  # Packing the checkbutton with padding
        self.date_entry.pack(padx=15, pady=15)  # Packing the date entry with padding
        
app = GUIApp()  # Creating an instance of GUIApp