# I18N
# Change the active language at runtime (using external language files - langpack v2)
# Language menu is dynamically populated with available languages

import tkinter as tk
from tkinter import ttk
import glob


class AddNewGrade(tk.Tk):  # Defining a class that inherits from tk.Tk

    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.selected_language = tk.StringVar(value="en")  # Set the default language
        self.i18n = I18N(self.selected_language.get())  # Load translations for the selected language
        self.geometry("330x165+550+250")  # Setting the window size and position
        self.title(self.i18n.translations["title"])  # Setting the window title
        self.iconbitmap("python.ico")  # Setting the window icon
        self.resizable(False, False)  # Disabling window resizing
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop

    def create_widgets(self):  # Method to create widgets
        self.lbl_fname = tk.Label(text=self.i18n.translations["fname"])
        self.lbl_lname = tk.Label(text=self.i18n.translations["lname"])
        self.lbl_grade = tk.Label(text=self.i18n.translations["grade"])
        
        self.txt_fname = ttk.Entry(self, width=35)
        self.txt_lname = ttk.Entry(self, width=35)
        self.txt_grade = ttk.Entry(self, width=35)
        
        self.btn_save = ttk.Button(self, text=self.i18n.translations["save"])
        
        self.context_menu = tk.Menu(self, tearoff=False)

        available_languages = self.i18n.get_available_languages()
        for lang_code in available_languages:
            lang_label = self.i18n.get_language_name(lang_code)
            self.context_menu.add_radiobutton(label=lang_label,
                                              value=lang_code,
                                              variable=self.selected_language,
                                              command= lambda: self.reload_gui_text())
        
        self.bind("<Button-2>", self.show_context_menu)
        
    def show_context_menu(self, event):  # Method to show context menu
        self.context_menu.post(event.x_root, event.y_root)  # Displaying the context menu at the cursor position

    def reload_gui_text(self):  # Method to reload GUI text
        self.i18n = I18N(self.selected_language.get())
        self.title(self.i18n.translations["title"])
        self.lbl_fname.configure(text=self.i18n.translations["fname"])
        self.lbl_lname.configure(text=self.i18n.translations["lname"])
        self.lbl_grade.configure(text=self.i18n.translations["grade"])
        self.btn_save.configure(text=self.i18n.translations["save"])
        
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
    
        

class I18N:
    def __init__(self, language_code):
        if language_code in self.get_available_languages():
            self.translations = self.load_data_from_file(language_code)
        else:
            raise NotImplementedError("Unsupported or missing lang file")
    
    @staticmethod
    def get_available_languages():
        language_files = glob.glob("*.lng")    
        language_codes =[]
        
        for f in language_files:
            language_code = f.replace("data_","").replace(".lng","")
            language_codes.append(language_code)
        return language_codes
    
    @staticmethod
    def load_data_from_file(language_code):
        language_file = f"data_{language_code}.lng"
        language_data = {}
        try:
            with open(language_file, encoding="utf-8") as f:
                for line in f:
                    (key,val) = line.strip().split("=")
                    language_data[key] = val
        except FileNotFoundError:
            raise ValueError("file not exist")
        return language_data
             
    @staticmethod
    def get_language_name(language_code):
        language_file = f"data_{language_code}.lng"
        try:
            with open(language_file, encoding="utf-8") as f:
                for line in f:
                    (key,val) = line.strip().split("=")
                    if key == "language":
                        return val
                raise ValueError("lang key not found")
        except FileNotFoundError:
            raise ValueError("language file not found")
        
app = AddNewGrade()