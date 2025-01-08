import tkinter as tk
from tkinter import ttk, messagebox as msg
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
    def __init__(self):
        super().__init__()
        self.geometry("330x165")
        self.title("Grade")
        self.resizable(False, False)
        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.grade = tk.IntVar()
        self.db = GradeBookDatabase()
        self.create_widgets()
        self.create_layout()
        self.mainloop()
        
    def create_widgets(self):
        self.lbl_fname = ttk.Label(self, text="First Name")
        self.lbl_lname = ttk.Label(self, text="Last Name")
        self.lbl_grade = ttk.Label(self, text="Grade")
        
        self.txt_fname = ttk.Entry(self, textvariable=self.fname, width=35)
        self.txt_lname = ttk.Entry(self, textvariable=self.lname, width=35)
        self.txt_grade = ttk.Entry(self, textvariable=self.grade, width=35)
        
        self.btn_save = ttk.Button(self, text="Save Grade", command=self.save_grade)
        self.btn_show_list = ttk.Button(self, text="Show list", command=self.show_list)
        
        self.txt_fname.focus_set()
        

    def create_layout(self):
        self.columnconfigure(index=0, weight=1, uniform="eq")
        self.columnconfigure(index=1, weight=3, uniform="eq")
        self.rowconfigure(index=0, weight=1, uniform="eq")
        self.rowconfigure(index=1, weight=1, uniform="eq")
        self.rowconfigure(index=2, weight=1, uniform="eq")
        self.rowconfigure(index=3, weight=1, uniform="eq")
        
        self.lbl_fname.grid(column=0, row=0)
        self.txt_fname.grid(column=1, row=0)
        
        self.lbl_lname.grid(column=0, row=1)
        self.txt_lname.grid(column=1, row=1)
        
        self.lbl_grade.grid(column=0, row=2)
        self.txt_grade.grid(column=1, row=2)
        
        self.btn_show_list.grid(column=0, row=3)
        self.btn_save.grid(column=1, row=3)

    def save_grade(self):
        if len(self.fname.get()) == 0 or len(self.lname.get()) == 0:
            msg.showerror(title="Error", message="Fill the form")
            return
        
        try:
            self.db.save_grade(fname=self.txt_fname.get(), lname=self.txt_lname.get(), grade=self.txt_grade.get())
            msg.showinfo("Done", "Grade saved")
            self.reset_text_boxes()
            self.txt_fname.focus_set()
        except (tk.TclError, OverflowError):
            msg.showerror("Error", "Unable to save")
            

    def reset_text_boxes(self):
        self.fname.set("")
        self.lname.set("")
        self.grade.set("")

    def show_list(self):
        ListGrades()

class ListGrades(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("450x200")
        self.title("List")
        self.db = GradeBookDatabase()
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
        
        self.tv.column("id", anchor="center", width=45)
        self.tv.column("fname", anchor="w", width=135)
        self.tv.column("lname", anchor="w", width=135)
        self.tv.column("grade", anchor="w", width=135)
        
        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.tv_scroll.set)
        
        self.bind("<F1>", self.show_average)
        self.tv.bind("<<TreeviewSelect>>", self.item_select)
        self.tv.bind("<F2>", self.delete_grade)
        self.tv.bind("<Double-1>", self.show_edit_window)

    def create_layout(self):
        self.tv.pack(fill="both", expand=True)
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

    def list_grades(self):
        grades = self.db.get_grades()
        for g in grades:
            self.tv.insert(parent="", index="end", values=g)

    def show_average(self, event):
        result = self.db.get_count_and_average()
        if result[0] == 0:
            msg_content = "Db is empty"
        else:
            msg_content = (f"Number of records: {result[0]}\n\n"
                           f"The average: {round(result[1], 1)}")
            msg.showinfo(title="count and average", message=msg_content)
            

    def item_select(self, event):
        for i in self.tv.selection():
            print(self.tv.item(i)["values"])

    def delete_grade(self, event):
        if len(self.tv.selection()) == 0:
            return
        
        answer = msg.askyesno(title="Sure?", message="sure to delete?")
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                self.db.delete_grade(selected_row[0])
                self.tv.delete(i)

    def show_edit_window(self, event):
        region=self.tv.identify("region", event.x, event.y)
        if region!= "cell":
            return
        selected_row_id = self.tv.selection()[0]
        selected_grade_row = self.tv.item(selected_row_id)["values"]
        self.edit_selected = EditGrade(parent=self,
                                       rowid=selected_row_id,
                                       gid=selected_grade_row[0],
                                       fname=selected_grade_row[1],
                                       lname=selected_grade_row[2],
                                       grade=selected_grade_row[3])
        self.edit_selected.grab_set()

class EditGrade(tk.Toplevel):
    def __init__(self, parent, rowid, gid, fname, lname, grade):
        super().__init__()
        self.geometry("330x165")
        self.title("Edit")
        self.parent = parent
        self.rowid = rowid
        self.gid = gid
        self.fname = fname
        self.lname = lname
        self.grade = grade
        self.db = GradeBookDatabase()
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.lbl_fname = ttk.Label(self, text="First Name")
        self.lbl_lname = ttk.Label(self, text="Last Name")
        self.lbl_grade = ttk.Label(self, text="Grade")
        
        self.txt_fname = ttk.Entry(self, textvariable=self.fname, width=35)
        self.txt_lname = ttk.Entry(self, textvariable=self.lname, width=35)
        self.txt_grade = ttk.Entry(self, textvariable=self.grade, width=35)
        
        self.btn_update = ttk.Button(self, text="update", command=self.update_values)
        
        self.txt_fname.focus_set()

    def create_layout(self):
        self.columnconfigure(index=0, weight=1, uniform="eq")
        self.columnconfigure(index=1, weight=3, uniform="eq")
        self.rowconfigure(index=0, weight=1, uniform="eq")
        self.rowconfigure(index=1, weight=1, uniform="eq")
        self.rowconfigure(index=2, weight=1, uniform="eq")
        self.rowconfigure(index=3, weight=1, uniform="eq")
        
        self.lbl_fname.grid(column=0, row=0)
        self.txt_fname.grid(column=1, row=0)
        
        self.lbl_lname.grid(column=0, row=1)
        self.txt_lname.grid(column=1, row=1)
        
        self.lbl_grade.grid(column=0, row=2)
        self.txt_grade.grid(column=1, row=2)
        
        self.btn_update.grid(column=0, row=3, columnspan=2)

    def update_values(self):
        if len(self.lname.get()) == 0:
            msg.showerror("error", "fill out")
            return
        try:
            self.db.update_grade(gid=self.gid, fname=self.fname.get(), lname=self.lname.get(), grade=self.grade.get())
            self.parent.tv.item(self.rowid, values=(self.gid, self.fname.get(), self.lname.get(), self.grade.get()))
            self.destroy()
        except (tk.TclError, OverflowError):
            msg.showerror("error", "Unable to update")

# Database setup and application launch
gradebook_db = GradeBookDatabase()
gradebook_db.create_table()
gradebook_db.fill_data()
app = AddNewGrade()