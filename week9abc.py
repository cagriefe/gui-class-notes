# GUI for inserting new records into the database.
# GUI for listing database content (Treeview with scrollbar and event bindings).
# GUI for editing records.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3

class GradeBookDatabase:

    def __init__(self, db_name="gradebook.db"):
        self.db_name = db_name

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("""
            create table if not exists GradeBook (
                gid   integer primary key autoincrement,
                fname text,
                lname text,
                grade integer
            );
            """)
        conn.commit()
        conn.close()

    def fill_data(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        data = [('Melissa', 'Bishop', 70),
                ('Linda', 'Scanlon', 55),
                ('Russel', 'Gruver', 60),
                ('Maria', 'Mayes', 100),
                ('Dennis', 'Hill', 95),
                ('Nathan', 'Martin', 40),
                ('William', 'Biggs', 85),
                ('Lois', 'Ballard', 60),
                ('Larry', 'Manning', 50),
                ('Dustin', 'Smalls', 30),
                ('Alice', 'Lucas', 70),
                ('John', 'Howell', 90)]

        for item in data:
            cur.execute("""insert into GradeBook(fname, lname, grade)
                        values(?, ?, ?)""", item)

        conn.commit()
        conn.close()

    def save_grade(self, fname, lname, grade):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("""insert into GradeBook(fname, lname, grade)
                    values(?, ?, ?)""",
                    (fname, lname, grade))
        conn.commit()
        conn.close()

    def get_grades(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("select * from GradeBook")
        grade_list = cur.fetchall()
        conn.close()

        return grade_list

    def get_count_and_average(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("select count(*), avg(grade) from GradeBook")
        result = cur.fetchone()
        conn.close()

        return result

    def delete_grade(self, gid):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("delete from GradeBook where gid=?", (gid, ))
        conn.commit()
        conn.close()

    def update_grade(self, gid, fname, lname, grade):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("update GradeBook set fname=?, lname=?, grade=? where gid=?",
                    (fname, lname, grade, gid))
        conn.commit()
        conn.close()

class AddNewGrade(tk.Tk):

    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.geometry("330x165+550+250")  # Setting the window size and position
        self.title("Week 9")  # Setting the window title
        self.iconbitmap("python.ico")  # Setting the window icon
        self.resizable(False, False)  # Disabling window resizing
        self.fname = tk.StringVar()  # Creating a StringVar for first name
        self.lname = tk.StringVar()  # Creating a StringVar for last name
        self.grade = tk.IntVar()  # Creating an IntVar for grade
        self.db = GradeBookDatabase()  # Creating an instance of the database
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
        self.btn_show_list = ttk.Button(self, text="Show list", command=self.show_list)
        
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
        self.btn_save.grid(column=1, row=3)  # Placing save button in grid
        self.btn_show_list.grid(column=0, row=3)
        
        
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
        
    def show_list(self):
        ListGrades()


class ListGrades(tk.Tk):  # Defining a class that inherits from tk.Tk

    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.geometry("450x200+550+250")  # Setting the window size and position
        self.title("Week 9")  # Setting the window title
        self.iconbitmap("python.ico")  # Setting the window icon
        self.db = GradeBookDatabase()  # Creating an instance of the database
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
        self.tv.bind("<F2>", self.delete_grade)  # Binding Delete key to delete_grade function
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
            
        answer = msg.askyesno(title="Confirm Delete", message="sure delete the selected row?")  # Asking for confirmation
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
        self.edit_selected = EditGrade(parent=self,
                                              rowid=selected_row_id,
                                              gid=selected_grade_row[0],
                                              fname=selected_grade_row[1],
                                              lname=selected_grade_row[2],
                                              grade=selected_grade_row[3])  # Creating an instance of EditGrade
        self.edit_selected.grab_set()  # Setting grab on the edit window


            
        
class EditGrade(tk.Toplevel):
    
    def __init__(self, parent, rowid, gid, fname, lname, grade):
        super().__init__()
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
        self.db = GradeBookDatabase()  # Creating an instance of the database
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
            self.db.update_grade(gid=self.gid, fname=self.fname.get(), 
                                 lname=self.lname.get(), grade=self.grade.get())
            # Update the Treeview row (that is in the parent window)
            self.parent.tv.item(self.rowid, values=(self.gid, self.fname.get(),
                                                    self.lname.get(), self.grade.get()))
            # Close the window
            self.destroy()
        except (tk.TclError, OverflowError):  # Handling exceptions
            msg.showerror("Error", "Unable to update data.")  # Showing error message
            
        
gradebook_db = GradeBookDatabase()
gradebook_db.create_table()
gradebook_db.fill_data()

app = AddNewGrade()