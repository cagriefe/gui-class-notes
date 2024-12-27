# GUI for listing database content (Treeview with scrollbar and event bindings).

import tkinter as tk  # Importing tkinter for GUI components
from tkinter import ttk  # Importing themed tkinter widgets
from tkinter import messagebox as msg  # Importing messagebox for displaying messages
import dblib  # Importing dblib for database operations
import week9c  # Importing week9c for additional functionality

class ListGrades(tk.Tk):  # Defining a class that inherits from tk.Tk

    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.geometry("450x200+550+250")  # Setting the window size and position
        self.title("Week 9")  # Setting the window title
        self.iconbitmap("python.ico")  # Setting the window icon
        self.db = dblib.GradeBookDatabase()  # Creating an instance of the database
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.list_grades()  # Calling method to list grades
        self.mainloop()  # Starting the main event loop

    def create_widgets(self):  # Method to create widgets
        self.tv = ttk.Treeview(self, height=10, show="headings")  # Creating a Treeview widget
        self.tv["columns"] = ("id", "fname", "lname", "grade")  # Defining columns
        self.tv["selectmode"] = "browse"  # Setting selection mode

        self.tv.heading("id", text="ID", anchor="center")  # Adding heading for ID column
        self.tv.heading("fname", text="First Name", anchor="center")  # Adding heading for First Name column
        self.tv.heading("lname", text="Last Name", anchor="center")  # Adding heading for Last Name column
        self.tv.heading("grade", text="Grade", anchor="center")  # Adding heading for Grade column

        self.tv.column("id", anchor="center", width=45, stretch=False)  # Configuring ID column
        self.tv.column("fname", anchor="w", width=135)  # Configuring First Name column
        self.tv.column("lname", anchor="w", width=135)  # Configuring Last Name column
        self.tv.column("grade", anchor="center", width=135)  # Configuring Grade column

        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)  # Adding a vertical scrollbar
        self.tv.configure(yscrollcommand=self.tv_scroll.set)  # Configuring Treeview to use scrollbar

        self.bind("<F1>", self.show_average)  # Binding F1 key to show_average function
        self.tv.bind("<<TreeviewSelect>>", self.item_select)  # Binding Treeview selection event to item_select function
        self.tv.bind("<Delete>", self.delete_grade)  # Binding Delete key to delete_grade function
        self.tv.bind("<Double-1>", self.show_edit_window)  # Binding double-click event to show_edit_window function

    def create_layout(self):  # Method to create layout
        self.tv.pack(fill="both", expand=True)  # Packing Treeview widget
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")  # Placing scrollbar

    def list_grades(self):  # Method to list grades
        grades = self.db.get_grades()  # Getting grades from database
        for g in grades:  # Looping through grades
            self.tv.insert(parent="", index="end", values=g)  # Inserting grade into Treeview

    def show_average(self, event):  # Method to show average grade
        result = self.db.get_count_and_average()  # Getting count and average from database

        if result[0] == 0:  # Checking if the database is empty
            msg_content = "The database is empty."  # Setting message content
        else:
            msg_content = (f"Number of recorded grades: {result[0]}\n\n"
                           f"The average: {round(result[1], 1)}")  # Setting message content

        msg.showinfo(title="Count and Average", message=msg_content)  # Showing info message

    def item_select(self, event):  # Method to handle item selection
        for i in self.tv.selection():  # Looping through selected items
            print(self.tv.item(i)["values"])  # Printing selected item values

    def delete_grade(self, event):  # Method to delete grade
        if len(self.tv.selection()) == 0:  # Checking if no rows are selected
            return  # Exiting the method
            
        answer = msg.askyesno(title="Confirm Delete", message="Are you sure you want to delete the selected row?")  # Asking for confirmation
        if answer:  # If confirmed
            for i in self.tv.selection():  # Looping through selected items
                selected_row = self.tv.item(i)["values"]  # Getting selected row values
                self.db.delete_grade(selected_row[0])  # Deleting grade from database
                self.tv.delete(i)  # Deleting grade from Treeview

    def show_edit_window(self, event):  # Method to show edit window
        region = self.tv.identify("region", event.x, event.y)  # Identifying region of the event
        if region != "cell":  # Checking if the region is not a cell
            return  # Exiting the method

        selected_row_id = self.tv.selection()[0]  # Getting selected row ID
        selected_grade_row = self.tv.item(selected_row_id)["values"]  # Getting selected grade row values
        self.edit_selected = week9c.EditGrade(parent=self,
                                              rowid=selected_row_id,
                                              gid=selected_grade_row[0],
                                              fname=selected_grade_row[1],
                                              lname=selected_grade_row[2],
                                              grade=selected_grade_row[3])  # Creating an instance of EditGrade
        self.edit_selected.grab_set()  # Setting grab on the edit window

app = ListGrades()  # Creating an instance of ListGrades