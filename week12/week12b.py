# I18N
# Change lang at runtime

import tkinter as tk  # Importing tkinter for GUI components
from tkinter import ttk  # Importing themed tkinter widgets
import langpack_v1  # Importing language pack for internationalization

class AddNewGrade(tk.Tk):  # Defining a class that inherits from tk.Tk
    
    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.selected_language = tk.StringVar(value="en")  # Setting the default language
        self.i18n = langpack_v1.I18N(self.selected_language.get())  # Loading translations for the selected language
        self.geometry("330x165+550+250")  # Setting the window size and position
        self.title(self.i18n.title)  # Setting the window title
        self.iconbitmap("python.ico")  # Setting the window icon
        self.resizable(False, False)  # Disabling window resizing
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop

    def create_widgets(self):  # Method to create widgets
        self.lbl_fname = tk.Label(self, text=self.i18n.fname)  # Creating label for first name
        self.lbl_lname = tk.Label(self, text=self.i18n.lname)  # Creating label for last name
        self.lbl_grade = tk.Label(self, text=self.i18n.grade)  # Creating label for grade

        self.txt_fname = ttk.Entry(self, width=35)  # Creating entry for first name
        self.txt_lname = ttk.Entry(self, width=35)  # Creating entry for last name
        self.txt_grade = ttk.Entry(self, width=35)  # Creating entry for grade

        self.btn_save = ttk.Button(self, text=self.i18n.save)  # Creating button to save grade
        
        # Context menu
        self.context_menu = tk.Menu(self, tearoff=False)  # Creating a context menu
        
        self.context_menu.add_radiobutton(label="English",
                                          value="en",
                                          variable=self.selected_language,
                                          command=lambda: self.reload_gui_text())  # Adding English option to context menu
        
        self.context_menu.add_radiobutton(label="Turkish",
                                          value="tr",
                                          variable=self.selected_language,
                                          command=lambda: self.reload_gui_text())  # Adding Turkish option to context menu

        self.bind("<Button-2>", self.show_context_menu)  # Binding right-click to show context menu
        
    def show_context_menu(self, event):  # Method to show context menu
        self.context_menu.post(event.x_root, event.y_root)  # Displaying the context menu at the cursor position
    
    def reload_gui_text(self):  # Method to reload GUI text
        self.i18n = langpack_v1.I18N(self.selected_language.get())  # Reloading translations for the selected language
        self.title(self.i18n.title)  # Updating the window title
        self.lbl_fname.configure(text=self.i18n.fname)  # Updating the first name label
        self.lbl_lname.configure(text=self.i18n.lname)  # Updating the last name label
        self.lbl_grade.configure(text=self.i18n.grade)  # Updating the grade label
        self.btn_save.configure(text=self.i18n.save)  # Updating the save button text
        
    def create_layout(self):  # Method to create layout
        self.columnconfigure(index=0, weight=1, uniform="eq")  # Configuring column 0
        self.columnconfigure(index=1, weight=3, uniform="eq")  # Configuring column 1
        self.rowconfigure(index=0, weight=1, uniform="eq")  # Configuring row 0
        self.rowconfigure(index=1, weight=1, uniform="eq")  # Configuring row 1
        self.rowconfigure(index=2, weight=1, uniform="eq")  # Configuring row 2
        self.rowconfigure(index=3, weight=1, uniform="eq")  # Configuring row 3

        self.lbl_fname.grid(column=0, row=0)  # Placing first name label in grid
        self.lbl_lname.grid(column=0, row=1)  # Placing last name label in grid
        self.lbl_grade.grid(column=0, row=2)  # Placing grade label in grid

        self.txt_fname.grid(column=1, row=0)  # Placing first name entry in grid
        self.txt_lname.grid(column=1, row=1)  # Placing last name entry in grid
        self.txt_grade.grid(column=1, row=2)  # Placing grade entry in grid
        self.btn_save.grid(column=0, row=3, columnspan=2)  # Placing save button in grid

app = AddNewGrade()  # Creating an instance of AddNewGrade