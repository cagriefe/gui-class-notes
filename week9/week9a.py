# GUI for inserting new records into the database.

import tkinter as tk  # Importing tkinter for GUI components
from tkinter import ttk  # Importing themed tkinter widgets
from tkinter import messagebox as msg  # Importing messagebox for displaying messages
import dblib  # Importing dblib for database operations


class AddNewGrade(tk.Tk):  # Defining a class that inherits from tk.Tk

    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.geometry("330x165+550+250")  # Setting the window size and position
        self.title("Week 9")  # Setting the window title
        self.iconbitmap("python.ico")  # Setting the window icon
        self.resizable(False, False)  # Disabling window resizing
        self.fname = tk.StringVar()  # Creating a StringVar for first name
        self.lname = tk.StringVar()  # Creating a StringVar for last name
        self.grade = tk.IntVar()  # Creating an IntVar for grade
        self.db = dblib.GradeBookDatabase()  # Creating an instance of the database
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop

    def create_widgets(self):  # Method to create widgets
        self.lbl_fname = tk.Label(self, text="First Name")  # Creating label for first name
        self.lbl_lname = tk.Label(self, text="Last Name")  # Creating label for last name
        self.lbl_grade = tk.Label(self, text="Grade")  # Creating label for grade

        self.txt_fname = ttk.Entry(self, textvariable=self.fname, width=35)  # Creating entry for first name
        self.txt_lname = ttk.Entry(self, textvariable=self.lname, width=35)  # Creating entry for last name
        self.txt_grade = ttk.Entry(self, textvariable=self.grade, width=35)  # Creating entry for grade

        self.btn_save = ttk.Button(self, text="Save Grade", command=self.save_grade)  # Creating button to save grade

        self.txt_fname.focus_set()  # Setting focus to first name entry

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

    def save_grade(self):  # Method to save grade
        if len(self.lname.get()) == 0 or len(self.fname.get()) == 0:  # Checking if any field is empty
            msg.showerror("Error", "Please fill out all fields in the form.")  # Showing error message
            return  # Exiting the method
            
        try:
            self.db.save_grade(fname=self.fname.get(), lname=self.lname.get(), grade=self.grade.get())  # Saving grade to database
            msg.showinfo("Done", "Grade saved.")  # Showing success message
            self.reset_text_boxes()  # Resetting text boxes
            self.txt_fname.focus_set()  # Setting focus to first name entry
        except (tk.TclError, OverflowError):  # Handling exceptions
            msg.showerror("Error", "Unable to save data.")  # Showing error message

    def reset_text_boxes(self):  # Method to reset text boxes
        self.fname.set("")  # Resetting first name
        self.lname.set("")  # Resetting last name
        self.grade.set(0)  # Resetting grade


app = AddNewGrade()  # Creating an instance of AddNewGrade