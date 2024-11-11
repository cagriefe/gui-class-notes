# GUI for inserting new records into the database.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

import dblib
class AddNewGrade(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent class (tk.Tk)
        self.geometry("330x165+550+250")  # Set the window size and position
        self.title("Week 7")  # Set the window title
        self.iconbitmap("python.ico")  # Set the window icon
        self.resizable(False, False)  # Disable window resizing
        self.fname = tk.StringVar()  # Create a StringVar for the first name
        self.lname = tk.StringVar()  # Create a StringVar for the last name
        self.grade = tk.IntVar()  # Create an IntVar for the grade
        self.db = dblib.GradeBookDatabase()  # Create an instance of the GradeBookDatabase class
        self.create_widgets()  # Call the method to create widgets
        self.create_layout()  # Call the method to create the layout
        self.mainloop()  # Start the main loop to run the application
    def create_widgets(self):
        # Create labels for first name, last name, and grade
        self.lbl_fname = tk.Label(self, text="First Name")
        self.lbl_lname = tk.Label(self, text="Last Name")
        self.lbl_grade = tk.Label(self, text="Grade")
        # Create entry fields for first name, last name, and grade
        self.txt_fname = ttk.Entry(self, textvariable=self.fname, width=35)
        self.txt_lname = ttk.Entry(self, textvariable=self.lname, width=35)
        self.txt_grade = ttk.Entry(self, textvariable=self.grade, width=35)
        # Create a button to save the grade
        self.btn_save = ttk.Button(self, text="Save Grade", command=self.save_grade)
        # Set focus to the first name entry field
        self.txt_fname.focus_set()
    def create_layout(self):
        # Configure the grid layout
        self.columnconfigure(index=0, weight=1, uniform="eq")
        """More"""
        # Place the labels and entry fields in the grid
        self.lbl_fname.grid(column=0, row=0)
        """"More""""
        
    def save_grade(self):
        # Validate input fields
        if len(self.lname.get()) == 0 or len(self.fname.get()) == 0:
            msg.showerror("Error", "Please fill out all fields in the form.")
            return
        try:
            # Save the grade to the database
            self.db.save_grade(fname=self.fname.get(), lname=self.lname.get(),
            grade=self.grade.get())
            msg.showinfo("Done", "Grade saved.")
            self.reset_text_boxes()  # Reset the entry fields
            self.txt_fname.focus_set()  # Set focus to the first name entry field
        except (tk.TclError, OverflowError):
            msg.showerror("Error", "Unable to save data.")
    def reset_text_boxes(self):
        # Reset the entry fields
        self.fname.set("")
        self.lname.set("")
        self.grade.set(0)
# Create an instance of the AddNewGrade class to run the application
app = AddNewGrade()

