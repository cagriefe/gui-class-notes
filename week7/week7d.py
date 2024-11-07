import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
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

        # Configure each column.
        self.tv.column("id", anchor="center", width=45, stretch=False)
        self.tv.column("fname", anchor="w", width=135)
        self.tv.column("lname", anchor="w", width=135)
        self.tv.column("grade", anchor="center", width=135)

        # Add a vertical scrollbar to the Treeview.
        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.tv_scroll.set)

        # Bind the F1 key to the function that shows the average grade.
        self.bind("<F1>", self.show_average)

        # Bind the Treeview selection event to the item_select function.
        self.tv.bind("<<TreeviewSelect>>", self.item_select)

        # Bind the Delete key to the function that deletes the selected row.
        self.tv.bind("<Delete>", self.delete_grade)

    def create_layout(self):
        # Pack the Treeview widget to fill the window.
        self.tv.pack(fill="both", expand=True)
        # Place the scrollbar next to the Treeview.
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

    def list_grades(self):
        # Retrieve grades from the database.
        grades = self.db.get_grades()
        for g in grades:
            # Populate the Treeview by adding values to the end of it.
            self.tv.insert(parent="", index="end", values=g)

    def show_average(self, event):
        # Retrieve the count and average of grades from the database.
        result = self.db.get_count_and_average()
        # Create a message with the count and average.
        msg_content = (f"Number of recorded grades: {result[0]}\n\n"
                       f"The average: {round(result[1], 1)}")
        # Show the message in an info dialog.
        msg.showinfo(title="Count and Average", message=msg_content)

    def item_select(self, event):
        # Print the selected items in the Treeview.
        for i in self.tv.selection():
            print(self.tv.item(i)["values"])

    def delete_grade(self, event):
        # Do nothing if no rows are selected.
        if len(self.tv.selection()) == 0:
            return
            
        # Ask for confirmation before deleting the selected row.
        answer = msg.askyesno(title="Confirm Delete", message="Are you sure you want to delete the selected row?")
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                # Delete the selected row from the database.
                self.db.delete_grade(selected_row[0])
                # Delete the selected row from the Treeview.
                self.tv.delete(i)

# Create an instance of the ListGrades class to run the application
app = ListGrades()