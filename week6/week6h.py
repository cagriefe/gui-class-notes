import tkinter as tk
from tkinter import ttk

class SecondWindow(tk.Toplevel):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Second Window")
        self.geometry("300x200+600+300")
        self.iconbitmap("python.ico")
        self.create_widgets()
        self.create_layout()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def create_widgets(self):
        # Create widgets for the second window
        self.lbl1 = ttk.Label(self, text="Second Window", font=("Tahoma", 16))
        self.lbl2 = ttk.Label(self, text="Enter your message and press <Return>.")
        self.entry1 = ttk.Entry(self)
        self.btn1 = ttk.Button(self, text="Close", command=self.close_window)

        # Bind the Return key to the entry widget
        self.entry1.bind("<Return>", self.return_key)
        self.entry1.focus_set()

    def create_layout(self):
        # Arrange the widgets in the second window
        self.lbl1.pack(pady=(20, 0))
        self.lbl2.pack(pady=(20, 0))
        self.entry1.pack(pady=(20, 0))
        self.btn1.pack(pady=(20, 0))

    def return_key(self, event):
        # Update the label text in the parent window with the message from the entry widget
        self.parent.lbl2.configure(text=f"Message from the second window: {self.entry1.get()}")
        self.close_window()

    def close_window(self):
        # Close the second window
        self.destroy()