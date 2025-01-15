import ttkbootstrap as ttk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

class WorkoutDatabase:
    def __init__(self, db_name="workouts.db"):
        self.db_name = db_name
        
    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS workouts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        workout_type TEXT,
                        calories_burned INTEGER,
                        duration INTEGER
                    )
                    """)
        conn.commit()
        conn.close()
    
    def add_workout(self, workout_type, calories_burned, duration):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("INSERT INTO workouts (workout_type, calories_burned, duration) VALUES (?, ?, ?)", 
                    (workout_type, calories_burned, duration))
        conn.commit()
        conn.close()
    
    def get_items(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("SELECT id, workout_type, calories_burned, duration FROM workouts")
        items = cur.fetchall()
        conn.close()
        return items

    def delete_workout(self, workout_id):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("DELETE FROM workouts WHERE id = ?", (workout_id,))
        conn.commit()
        conn.close()

    def update_workout(self, workout_id, workout_type, calories_burned, duration):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("UPDATE workouts SET workout_type = ?, calories_burned = ?, duration = ? WHERE id = ?", 
                    (workout_type, calories_burned, duration, workout_id))
        conn.commit()
        conn.close()

    def get_calories_by_workout_type(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("SELECT workout_type, SUM(calories_burned) FROM workouts GROUP BY workout_type")
        items = cur.fetchall()
        conn.close()
        return items

class WorkoutManagement(ttk.Window):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Workout Management System")
        self.db = WorkoutDatabase()
        self.db.create_table()
        self.create_widgets()
        self.create_layout()
        self.refresh_list()
        self.mainloop()
    
    def create_widgets(self):
        self.lbl_workout_type = ttk.Label(self, text="Workout Type")
        self.lbl_calories_burned = ttk.Label(self, text="Calories Burned")
        self.lbl_duration = ttk.Label(self, text="Duration (minutes)")
        
        self.cmb_workout_type = ttk.Combobox(self, values=["Running", "Cycling", "Swimming", "Yoga", "Weightlifting"])
        self.cmb_workout_type.set("Select Workout Type")
        
        self.scl_calories_burned = ttk.Scale(self, from_=0, to=1000, orient="horizontal")
        self.scl_duration = ttk.Scale(self, from_=0, to=180, orient="horizontal")
        
        self.btn_add = ttk.Button(self, text="Add Workout", command=self.add_workout)
        self.btn_clear = ttk.Button(self, text="Clear Fields", command=self.clear_fields)
        
        self.tv = ttk.Treeview(self, columns=("ID", "Workout Type", "Calories Burned", "Duration"), show="headings", selectmode="browse")
        self.tv.heading("ID", text="ID")
        self.tv.heading("Workout Type", text="Workout Type")
        self.tv.heading("Calories Burned", text="Calories Burned")
        self.tv.heading("Duration", text="Duration")
        
        self.btn_update = ttk.Button(self, text="Update Workout", command=self.update_workout)
        self.btn_delete = ttk.Button(self, text="Delete Workout", command=self.delete_workout)
        self.btn_show_chart = ttk.Button(self, text="Show Chart", command=self.show_chart)
        
    def create_layout(self):
        self.columnconfigure(index=0, weight=1, uniform="eq")
        self.columnconfigure(index=1, weight=1, uniform="eq")
        self.rowconfigure(index=0, weight=1, uniform="eq")
        self.rowconfigure(index=1, weight=1, uniform="eq")
        self.rowconfigure(index=2, weight=1, uniform="eq")
        self.rowconfigure(index=3, weight=1, uniform="eq")
        self.rowconfigure(index=4, weight=6, uniform="eq")
        self.rowconfigure(index=5, weight=1, uniform="eq")
        
        self.lbl_workout_type.grid(column=0, row=0)
        self.cmb_workout_type.grid(column=1, row=0)
        
        self.lbl_calories_burned.grid(column=0, row=1)
        self.scl_calories_burned.grid(column=1, row=1)
        
        self.lbl_duration.grid(column=0, row=2)
        self.scl_duration.grid(column=1, row=2)
        
        self.btn_add.grid(column=0, row=3)
        self.btn_clear.grid(column=1, row=3)
        
        self.tv.grid(column=0, row=4, columnspan=2)
        
        self.btn_delete.grid(column=0, row=5)
        self.btn_update.grid(column=1, row=5)
        self.btn_show_chart.grid(column=0, row=6, columnspan=2)
        
    def add_workout(self):
        workout_type = self.cmb_workout_type.get()
        calories_burned = int(self.scl_calories_burned.get())
        duration = int(self.scl_duration.get())
        if workout_type != "Select Workout Type" and calories_burned and duration:
            self.db.add_workout(workout_type, calories_burned, duration)
            self.refresh_list()
            self.clear_fields()
        else:
            messagebox.showerror("Input error", "All fields are required.")
    
    def clear_fields(self):
        self.cmb_workout_type.set("Select Workout Type")
        self.scl_calories_burned.set(0)
        self.scl_duration.set(0)
    
    def update_workout(self):
        selected_item = self.tv.selection()
        if selected_item:
            workout_id = self.tv.item(selected_item, "values")[0]
            if workout_id:
                try:
                    workout_id = int(workout_id)
                    workout_type = self.cmb_workout_type.get()
                    calories_burned = int(self.scl_calories_burned.get())
                    duration = int(self.scl_duration.get())
                    if workout_type != "Select Workout Type" and calories_burned and duration:
                        self.db.update_workout(workout_id, workout_type, calories_burned, duration)
                        self.refresh_list()
                        self.clear_fields()
                    else:
                        messagebox.showerror("Input error", "All fields are required.")
                except ValueError:
                    messagebox.showerror("Error", "Invalid workout ID.")
    
    def delete_workout(self):
        selected_item = self.tv.selection()
        if selected_item:
            workout_id = self.tv.item(selected_item, "values")[0]
            if workout_id:
                try:
                    workout_id = int(workout_id)
                    self.db.delete_workout(workout_id)
                    self.refresh_list()
                except ValueError:
                    messagebox.showerror("Error", "Invalid workout ID.")
    
    def refresh_list(self):
        for item in self.tv.get_children():
            self.tv.delete(item)
            
        for row in self.db.get_items():
            self.tv.insert(parent="", index="end", iid=row[0], values=(row[0], row[1], row[2], row[3]))
    
    def show_chart(self):
        data = self.db.get_calories_by_workout_type()
        workout_types = [row[0] for row in data]
        calories = [row[1] for row in data]
        running = [data[1] for row in data]
        
        plt.figure(figsize=(10, 6))
        plt.bar(workout_types, calories, color='skyblue')
        plt.xlabel('Workout Type')
        plt.ylabel('Total Calories Burned')
        plt.title('Calories Burned by Workout Type')
        plt.show()
        
app = WorkoutManagement()