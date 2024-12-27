# GUI for editing records.

import tkinter as tk  # Importing tkinter for GUI components
from tkinter import ttk  # Importing themed tkinter widgets
from tkinter import messagebox as msg  # Importing messagebox for displaying messages
import dblib  # Importing dblib for database operations

class EditGrade(tk.Toplevel):  # Defining a class that inherits from tk.Toplevel

    def __init__(self, parent, rowid, gid, fname, lname, grade):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.geometry("330x165+600+300")  # Setting the window size and position
        self.title("Week 9")  # Setting the window title
        self.iconbitmap("python.ico")  # Setting the window icon
        self.resizable(False, False)  # Disabling window resizing
        self.parent = parent  # Storing reference to parent window
        self.rowid = rowid  # ID of the Treeview item that is currently being edited
        self.gid = gid  # Grade ID
        self.fname = tk.StringVar(value=fname)  # Creating a StringVar for first name with initial value
        self.lname = tk.StringVar(value=lname)  # Creating a StringVar for last name with initial value
        self.grade = tk.IntVar(value=grade)  # Creating an IntVar for grade with initial value
        self.db = dblib.GradeBookDatabase()  # Creating an instance of the database
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout

    def create_widgets(self):  # Method to create widgets
        self.lbl_fname = tk.Label(self, text="First Name")  # Creating label for first name
        self.lbl_lname = tk.Label(self, text="Last Name")  # Creating label for last name
        self.lbl_grade = tk.Label(self, text="Grade")  # Creating label for grade

        self.txt_fname = ttk.Entry(self, textvariable=self.fname, width=35)  # Creating entry for first name
        self.txt_lname = ttk.Entry(self, textvariable=self.lname, width=35)  # Creating entry for last name
        self.txt_grade = ttk.Entry(self, textvariable=self.grade, width=35)  # Creating entry for grade

        self.btn_update = ttk.Button(self, text="Update", command=self.update_values)  # Creating button to update values

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
        self.btn_update.grid(column=0, row=3, columnspan=2)  # Placing update button in grid

    def update_values(self):  # Method to update values
        if len(self.lname.get()) == 0 or len(self.fname.get()) == 0:  # Checking if any field is empty
            msg.showerror("Error", "Please fill out all fields in the form.")  # Showing error message
            return  # Exiting the method
            
        try:
            # Update the database
            self.db.update_grade(gid=self.gid, fname=self.fname.get(), lname=self.lname.get(), grade=self.grade.get())
            # Update the Treeview row (that is in the parent window)
            self.parent.tv.item(self.rowid, values=(self.gid, self.fname.get(), self.lname.get(), self.grade.get()))
            # Close the window
            self.destroy()
        except (tk.TclError, OverflowError):  # Handling exceptions
            msg.showerror("Error", "Unable to update data.")  # Showing error message