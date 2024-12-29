import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Study 8")
        self.geometry("300x200+300+200")
        self.create_widget()
        self.create_layout()
        self.mainloop()
        
    def create_widget(self):
        self.lbl1 = ttk.Label(self, text="Main window")
        self.btn1 = ttk.Button(self, text="Open Second Window",
                               command=self.open_new_window)
        self.btn2 = ttk.Button(self, text="Close", command=self.destroy)
        
    def create_layout(self):
        self.lbl1.pack(pady=(20,0))
        self.btn1.pack(pady=(20,0))
        self.btn2.pack(pady=(20,0))
    
    def open_new_window(self):
        self.win2 = SecondWindow(parent=self)
        self.win2.grab_set()
        
class SecondWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Study 8")
        self.geometry("300x200+300+200")
        self.create_widget()
        self.create_layout()
        self.mainloop()
        
    def create_widget(self):
        self.lbl1 = ttk.Label(self, text="Main window")
        self.btn1 = ttk.Button(self, text="Do nothing")
        self.btn2 = ttk.Button(self, text="Close", command=self.destroy)
        
    def create_layout(self):
        self.lbl1.pack(pady=(20,0))
        self.btn1.pack(pady=(20,0))
        self.btn2.pack(pady=(20,0))
    
    def open_new_window(self):
        self.win2 = SecondWindow(parent=self)
        self.win2.grab_set()
        
        
app = MainWindow()