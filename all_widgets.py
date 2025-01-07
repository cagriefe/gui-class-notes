import tkinter as tk
from tkinter import ttk

class WidgetShowcaseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Widget Showcase")
        self.geometry("800x600")
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_container = ttk.Frame(self)
        main_container.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Notebook for different sections
        notebook = ttk.Notebook(main_container)
        notebook.pack(expand=True, fill='both')
        
        # Basic widgets section
        basic_frame = ttk.Frame(notebook)
        notebook.add(basic_frame, text="Basic Widgets")
        
        # Labels
        ttk.Label(basic_frame, text="Standard Label").pack(pady=5)
        ttk.Label(basic_frame, text="Header Label", font=('Helvetica', 16, 'bold')).pack(pady=5)
        
        # Buttons
        ttk.Button(basic_frame, text="Standard Button").pack(pady=5)
        tk.Button(basic_frame, text="Classic Button").pack(pady=5)
        
        # Entry
        entry_frame = ttk.LabelFrame(basic_frame, text="Entry Widgets")
        entry_frame.pack(fill='x', padx=5, pady=5)
        ttk.Entry(entry_frame).pack(padx=5, pady=5)
        
        # Data display section
        data_frame = ttk.Frame(notebook)
        notebook.add(data_frame, text="Data Display")
        
        # Treeview
        tree = ttk.Treeview(data_frame, columns=("col1", "col2"), show="headings")
        tree.heading("col1", text="Column 1")
        tree.heading("col2", text="Column 2")
        tree.pack(expand=True, fill='both', padx=5, pady=5)
        
        # Input controls section
        input_frame = ttk.Frame(notebook)
        notebook.add(input_frame, text="Input Controls")
        
        # Checkbuttons
        ttk.Checkbutton(input_frame, text="Option 1").pack(pady=5)
        ttk.Checkbutton(input_frame, text="Option 2").pack(pady=5)
        
        # Radio buttons
        radio_var = tk.StringVar()
        ttk.Radiobutton(input_frame, text="Choice 1", variable=radio_var, value="1").pack(pady=5)
        ttk.Radiobutton(input_frame, text="Choice 2", variable=radio_var, value="2").pack(pady=5)
        
        # Combobox
        ttk.Combobox(input_frame, values=["Item 1", "Item 2", "Item 3"]).pack(pady=5)
        
        # Menu demo
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

if __name__ == "__main__":
    app = WidgetShowcaseApp()
    app.mainloop()