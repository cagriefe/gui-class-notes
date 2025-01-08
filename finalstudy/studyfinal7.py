import matplotlib.pyplot as plt
import sqlite3
import ttkbootstrap as ttk
from tkinter import messagebox as msg
import tkinter as tk

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
            cur.execute("insert into GradeBook(fname, lname, grade) values(?, ?, ?)", item)

        conn.commit()
        conn.close()

    def save_grade(self, fname, lname, grade):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("insert into GradeBook(fname, lname, grade) values(?, ?, ?)", (fname, lname, grade))
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
        # cur.execute("delete from GradeBook where gid=:gid", {"gid": gid})
        conn.commit()
        conn.close()

    def update_grade(self, gid, fname, lname, grade):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("update GradeBook set fname=?, lname=?, grade=? where gid=?",
                    (fname, lname, grade, gid))
        conn.commit()
        conn.close()
        

class GradeBook(ttk.Window):
    def __init__(self):
        super().__init__()
        self.geometry("450x200")
        self.title("Grade Book")
        self.resizable(False, False)
        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.grade = tk.IntVar()
        self.db = GradeBookDatabase()
        self.create_widgets()
        self.create_layout()
        self.list_grades()
        self.mainloop()
        
    def create_widgets(self):
        self.tv = ttk.Treeview(self, show="headings", selectmode="browse")
        self.tv["columns"] = ("id","fname","lname","grade")
        
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
        self.bind("<<TreeviewSelect>>", self.item_select)
        self.bind("<Delete>", self.delete_grade)
        self.bind("<F2>", self.show_chart)

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
            msg_content = (f"Num of records: {result[0]}\n\n"
                           f"The average: {round(result[1], 1)}")
        msg.showinfo(title="Count and Average", message=msg_content)
        
    def item_select(self, event):
        for i in self.tv.selection():
            print(self.tv.item(i)["values"])
            
    def delete_grade(self, event):
        if len(self.tv.selection()) == 0:
            return
        
        answer = msg.askyesno(title="Confirm?", message="Are u sure to delete?")
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                self.db.delete_grade(selected_row[0])
                self.tv.delete(i)
    
    def show_chart(self, event):
        grades = self.db.get_grades()
        grade_ranges = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        
        for g in grades:
            grade = g[3]
            if 90 <= grade <= 100:
                grade_ranges['A'] += 1
            elif 80 <= grade < 90:
                grade_ranges['B'] += 1
            elif 70 <= grade < 80:
                grade_ranges['C'] += 1
            elif 60 <= grade < 70:
                grade_ranges['D'] += 1
            else:
                grade_ranges['F'] += 1
        
        labels = grade_ranges.keys()
        sizes = grade_ranges.values()
        
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Grade Distribution')
        plt.show()
        
        
    
    
app = GradeBook()