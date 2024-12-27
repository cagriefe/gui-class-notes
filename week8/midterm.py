
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg


class Midterm(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("230x260+550+250")
        self.title("Midterm")
        self.iconbitmap("python.ico")
        self.resizable(False, False)
        self.weight = tk.IntVar()
        self.activity_level = tk.StringVar(value="Sedentary")
        self.climate = tk.StringVar(value="Mild")
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        self.lbl_title = ttk.Label(self, text="Daily Water Intake Calculator", font=("Tahoma", 12))

        self.lbl_weight = ttk.Label(self, text="Weight (kg):")
        self.lbl_activity = ttk.Label(self, text="Activity Level:")
        self.lbl_climate = ttk.Label(self, text="Climate:")

        self.txt_weight = ttk.Entry(self, textvariable=self.weight, width=30)
        self.cb_activity = ttk.Combobox(self, textvariable=self.activity_level, values=["Sedentary", "Moderate", "High"], state="readonly", width=27)
        self.cb_climate = ttk.Combobox(self, textvariable=self.climate, values=["Cold", "Mild", "Hot"], state="readonly", width=27)

        self.btn_calc = ttk.Button(self, text="Calculate", command=self.calc)

        self.bind("<Return>", self.do_calc)
        self.bind("<Escape>", self.exit_app)

    def create_layout(self):
        self.lbl_title.pack(pady=15)

        self.lbl_weight.pack()
        self.txt_weight.pack(pady=(0, 15))

        self.lbl_activity.pack()
        self.cb_activity.pack(pady=(0, 15))

        self.lbl_climate.pack()
        self.cb_climate.pack(pady=(0, 15))

        self.btn_calc.pack()

    def validate(self):
        try:
            if self.weight.get() <= 0:
                msg.showerror("Invalid Input", "Weight must be a positive number.")
                return False
        except tk.TclError:
            msg.showerror("Invalid Input", "Please enter a valid integer for weight.")
            return False

        return True

    def calc(self):
        if self.validate():
            base_intake = self.weight.get() * 0.033
            if self.activity_level.get() == "Moderate":
                base_intake += 0.5
            elif self.activity_level.get() == "High":
                base_intake += 1.0

            if self.climate.get() == "Mild":
                base_intake += 0.3
            elif self.climate.get() == "Hot":
                base_intake += 0.7

            result = f"Recommended daily water intake is {base_intake:.1f} liters."
            msg.showinfo("Result", result)

    def exit_app(self, event):
        self.destroy()

    def do_calc(self, event):
        self.calc()

app = Midterm()
