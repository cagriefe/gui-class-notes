import tkinter as tk
from tkinter import ttk
import dblib

class ListGrades(tk.Tk):
    
    def __init__(self):
        super().__init__()  # Initialize the parent class (tk.Tk)
        self.geometry("450x200+550+250")  # Set the window size and position
        self.title("Week 7")  # Set the window title
        self.iconbitmap("python.ico")  # Set the window icon
        self.db = dblib.GradeBookDatabase()  # Create an instance of the GradeBookDatabase class
        self.create_widgets()  # Call the method to create widgets
        self.create_layout()  # Call the method to create the layout
        self.list_grades()  # Call the method to list grades in the Treeview
        self.mainloop()  # Start the main loop to run the application
        
    def create_widgets(self):
        # Create a Treeview widget.
        # selectmode: extended(default), browse, none
        self.tv = ttk.Treeview(self, height=10, show="headings")
        self.tv["columns"] = ("id", "fname", "lname", "grade")
        self.tv["selectmode"] = "browse"
        
        # Add headings for each column.
        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("fname", text="First Name", anchor="center")
        self.tv.heading("lname", text="Last Name", anchor="center")
        self.tv.heading("grade", text="Grade", anchor="center")
        
        # Configure the columns.
        self.tv.column("id", anchor="center", width=45, stretch=False)
        self.tv.column("fname", anchor="w", width=135)
        self.tv.column("lname", anchor="w", width=135)
        self.tv.column("grade", anchor="center", width=135)
        
    def create_layout(self):
        # Pack the Treeview widget to fill the window.
        self.tv.pack(fill="both", expand=True)
    
    def list_grades(self):
        # Retrieve grades from the database.
        grades = self.db.get_grades()
        for g in grades:
            # Populate the Treeview by adding values to the end of it.
            self.tv.insert(parent="", index="end", values=g)
            
# Create an instance of the ListGrades class to run the application
app = ListGrades()