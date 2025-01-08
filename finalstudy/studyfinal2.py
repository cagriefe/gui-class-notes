import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3


class Quiz4:

    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Quiz 4")
        self.win.geometry("360x240+700+290")
        self.win.resizable(False, False)

        self.input_value = tk.StringVar()
        self.conversion_type = tk.IntVar()
        self.conversion_type.set(1)

        self.create_widgets()
        self.input_entry.focus_set()

    def get_db_connection(self):
        return sqlite3.connect("quiz4.db")

    def create_db_table(self):
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            cur.execute("""
            CREATE TABLE ConversionHistory (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            conversion_text TEXT
            );
            """)
            conn.commit()
            conn.close()
            msg.showinfo("Setup Database", "Database table created.")
        except Exception as exc:
            msg.showerror("Error", "Error: " + str(exc))

    def clear_history(self):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute("""
                    delete from ConversionHistory
                    """)
        conn.commit()
        conn.close()


    def show_history(self):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute("""
                    select cid, conversion_text from ConversionHistory
                    """)
        items = cur.fetchall()
        conn.close()

        if items:
            history_message = f"Total conversions: {len(items)}\n\n"
            for item in items:
                history_message += f"{item[0]}. {item[1]}\n"
        else:
            history_message = "Nothing has been converted yet."

        msg.showinfo("Conversion History", history_message)
        
    def add_to_database(self, result):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute("insert into ConversionHistory (conversion_text) values (?)", (result,))
        conn.commit()
        conn.close()
    
        
    def convert(self):
        
        try:
            x = float(self.input_value.get())

            if self.conversion_type.get() == 1:
                result = round((x * (9 / 5)) + 32, 1)
                result_string = f"{x} Celsius = {result} Fahrenheit"
            else:
                result = round((x - 32) * (5 / 9), 1)
                result_string = f"{x} Fahrenheit = {result} Celsius"

            msg.showinfo("Result", result_string)
        except Exception as exc:
            msg.showerror("Error", "Error: " + str(exc))
        
        if result_string:
            self.add_to_database(result_string)

    def create_widgets(self):
        ttk.Label(self.win, text="Temperature").grid(column=0, row=0, padx=20, pady=20)

        self.input_entry = ttk.Entry(self.win, textvariable=self.input_value)
        self.input_entry.grid(column=1, row=0, padx=20, pady=20)

        ttk.Label(self.win, text="Convert").grid(column=0, row=1)

        self.radio1 = ttk.Radiobutton(self.win, text="Celsius to Fahrenheit", variable=self.conversion_type, value=1)
        self.radio1.grid(column=1, row=1)
        self.radio2 = ttk.Radiobutton(self.win, text="Fahrenheit to Celsius", variable=self.conversion_type, value=2)
        self.radio2.grid(column=1, row=2)

        self.convert_btn = ttk.Button(self.win, text="Convert", width=35, command=self.convert)
        self.convert_btn.grid(column=0, row=3, columnspan=2, pady=20)

        self.history_btn = ttk.Button(self.win, text="History", width=35, command=self.show_history)
        self.history_btn.grid(column=0, row=4, columnspan=2)

        ttk.Label(self.win, text="Press F1 to setup database and F2 to clear history.").grid(column=0, row=5, columnspan=2, pady=10)

        
        # Bind "Enter" key to input_entry widget to trigger the convert method.
        self.win.bind("<Return>", lambda _ : self.convert())
        
        
        # Bind "F1" key to main window to trigger the create_db_table method.
        self.win.bind("<F1>", lambda _ : self.create_db_table())
        
        # TODO
        # Bind "F2" key to main window to trigger the clear_history method.
        self.win.bind("<F2>", lambda _ : self.clear_history())


app = Quiz4()
app.win.mainloop()