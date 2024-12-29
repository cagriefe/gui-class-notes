# I18N
# Basic implementation

import tkinter as tk  # Importing tkinter for GUI components
from tkinter import ttk  # Importing themed tkinter widgets
import langpack_v1  # Importing language pack for internationalization

class AddNewGrade(tk.Tk):  # Defining a class that inherits from tk.Tk

    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.i18n = langpack_v1.I18N("tr")  # Load language "tr", "en"
        self.geometry("330x165+550+250")  # Setting the window size and position
        self.title(self.i18n.title)  # Setting the window title
        self.iconbitmap("python.ico")  # Setting the window icon
        self.resizable(False, False)  # Disabling window resizing
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop

    def create_widgets(self):  # Method to create widgets
        self.lbl_fname = tk.Label(self, text=self.i18n.fname)  # Creating label for first name
        self.lbl_lname = tk.Label(self, text=self.i18n.lname)  # Creating label for last name
        self.lbl_grade = tk.Label(self, text=self.i18n.grade)  # Creating label for grade

        self.txt_fname = ttk.Entry(self, width=35)  # Creating entry for first name
        self.txt_lname = ttk.Entry(self, width=35)  # Creating entry for last name
        self.txt_grade = ttk.Entry(self, width=35)  # Creating entry for grade

        self.btn_save = ttk.Button(self, text=self.i18n.save)  # Creating button to save grade

    def create_layout(self):  # Method to create layout
        self.columnconfigure(index=0, weight=1, uniform="eq")  # Configuring column 0
        self.columnconfigure(index=1, weight=3, uniform="eq")  # Configuring column 1
        self.rowconfigure(index=0, weight=1, uniform="eq")  # Configuring row 0
        self.rowconfigure(index=1, weight=1, uniform="eq")  # Configuring row 1
        self.rowconfigure(index=2, weight=1, uniform="eq")  # Configuring row 2
        self.rowconfigure(index=3, weight=1, uniform="eq")  # Configuring row 3

        self.lbl_fname.grid(column=0, row=0)  # Placing first name label in grid
        self.lbl_lname.grid(column=0, row=1)  # Placing last name label in grid
        self.lbl_grade.grid(column=0, row=2)  # Placing grade label in grid

        self.txt_fname.grid(column=1, row=0)  # Placing first name entry in grid
        self.txt_lname.grid(column=1, row=1)  # Placing last name entry in grid
        self.txt_grade.grid(column=1, row=2)  # Placing grade entry in grid
        self.btn_save.grid(column=0, row=3, columnspan=2)  # Placing save button in grid

app = AddNewGrade()  # Creating an instance of AddNewGrade