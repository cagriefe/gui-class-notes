import tkinter as tk
from tkinter import ttk
import week6h  # Import the module containing the SecondWindow class

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Week 6")
        self.geometry("300x200+550+250")
        self.iconbitmap("python.ico")
        self.create_widgets()
        self.create_layout()
        self.mainloop()

    def create_widgets(self):
        # Create widgets for the main window
        self.lbl1 = ttk.Label(self, text="Main Window", font=("Tahoma", 16))
        self.lbl2 = ttk.Label(self)
        self.btn1 = ttk.Button(self, text="Open Second Window", command=self.open_new_window)
        self.btn2 = ttk.Button(self, text="Close", command=self.destroy)

    def create_layout(self):
        # Arrange the widgets in the main window
        self.lbl1.pack(pady=(20, 0))
        self.btn1.pack(pady=(20, 0))
        self.btn2.pack(pady=(20, 0))
        self.lbl2.pack(pady=(20, 0))

    def open_new_window(self):
        # Open the second window and restrict user interactions to it
        self.win2 = week6h.SecondWindow(parent=self)
        self.win2.grab_set()

# Create an instance of the MainWindow class to run the application
app = MainWindow()