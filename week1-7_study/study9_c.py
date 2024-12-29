import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import study9_a

class ListGrades(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry("450x200+550+250")
        self.title("Week 7")
        self.iconbitmap("python.ico")
        self.db = study9_a.GradeBookDatabase()
        self.create_widgets()
        self.create_layout()
        self.list_grades()
        self.mainloop()
        
    def create_widgets(self):
        self.tv = ttk.Treeview(self, height=10, show="headings")
        self.tv["columns"] = ("id", "fname", "lname", "grade")
        self.tv["selectmode"] = "browse"
        
        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("fname", text="First Name", anchor="center")
        self.tv.heading("lname", text="Last Name", anchor="center")
        self.tv.heading("grade", text="Grade", anchor="center")
        
        self.tv.column("id", anchor="center", width=45, stretch=False)
        self.tv.column("fname", anchor="w", width=135)
        self.tv.column("lname", anchor="w", width=135)
        self.tv.column("grade", anchor="center", width=135)
        
        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.tv_scroll.set)
        
        self.bind("<F1>", self.show_average)
        
        self.tv.bind("<<TreeviewSelect>>", self.item_select)
        
        self.tv.bind("<Delete>", self.delete_grade)
        
    def create_layout(self):
        self.tv.pack(fill="both", expand=True)
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

    def list_grades(self):
        grades = self.db.get_grades()
        for g in grades:
            self.tv.insert(parent="", index="end", values=g)
            
    def show_average(self, event):
        result = self.db.get_count_and_average()
        msg_content = (f"Number of recorded grades: {result[0]}\n\n"
                       f"The average: {round(result[1], 1)}")
        msg.showinfo(title="Count and Average", message=msg_content)

    def item_select(self, event):
        # print(self.tv.selection())
        for i in self.tv.selection():
            # print(self.tv.item(i))
            print(self.tv.item(i)["values"])

    def delete_grade(self, event):
        if len(self.tv.selection()) == 0: # Do nothing if no rows are selected.
            return
            
        answer = msg.askyesno(title="Confirm Delete", message="Are you sure you want to delete the selected row?")
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                self.db.delete_grade(selected_row[0])
                self.tv.delete(i)


app = ListGrades()

        