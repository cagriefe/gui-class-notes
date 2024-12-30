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
        self.lbl_fname = tk.Label(self, text=self.i18n.translations["fname"])  # Creating label for first name
        self.lbl_lname = tk.Label(self, text=self.i18n.translations["lname"])  # Creating label for last name
        self.lbl_grade = tk.Label(self, text=self.i18n.translations["grade"])  # Creating label for grade

        self.txt_fname = ttk.Entry(self, width=35)  # Creating entry for first name
        self.txt_lname = ttk.Entry(self, width=35)  # Creating entry for last name
        self.txt_grade = ttk.Entry(self, width=35)  # Creating entry for grade

        self.btn_save = ttk.Button(self, text=self.i18n.translations["save"])  # Creating button to save grade

        # Add a context menu
        self.context_menu = tk.Menu(self, tearoff=False)  # Creating a context menu

        # Populate the context menu with available language names ("de", "en", "fr", "tr")
        available_languages = self.i18n.get_available_languages()
        for lang_code in available_languages:
            lang_label = self.i18n.get_language_name(lang_code)
            self.context_menu.add_radiobutton(label=lang_label,
                                              value=lang_code,
                                              variable=self.selected_language,
                                              command=lambda: self.reload_gui_text())

        # Bind mouse right-click event to display the context menu
        self.bind("<Button-2>", self.show_context_menu)

    def show_context_menu(self, event):  # Method to show context menu
        self.context_menu.post(event.x_root, event.y_root)  # Displaying the context menu at the cursor position

    def reload_gui_text(self):  # Method to reload GUI text
        self.i18n = I18N(self.selected_language.get())  # Reloading translations for the selected language
        self.title(self.i18n.translations["title"])  # Updating the window title
        self.lbl_fname.configure(text=self.i18n.translations["fname"])  # Updating the first name label
        self.lbl_lname.configure(text=self.i18n.translations["lname"])  # Updating the last name label
        self.lbl_grade.configure(text=self.i18n.translations["grade"])  # Updating the grade label
        self.btn_save.configure(text=self.i18n.translations["save"])  # Updating the save button text

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
        if language_code in self.get_available_languages():  # Checking if the language is available
            self.translations = self.load_data_from_file(language_code)  # Loading translations from file
        else:
            raise NotImplementedError("Unsupported or missing lang file")  # Raising error for unsupported or missing language file
    
    @staticmethod
    def get_available_languages():
        language_files = glob.glob("*.lng")  # Getting all .lng files
        language_codes = []
        
        for f in language_files:
            language_code = f.replace("data_","").replace(".lng","")  # Extracting language code from file name
            language_codes.append(language_code)
            
        return language_codes  # Returning available language codes
    
    @staticmethod
    def load_data_from_file(language_code):
        language_file = f"data_{language_code}.lng"  # Constructing file name
        language_data = {}
        try:
            with open(language_file, encoding="utf-8") as f:  # Opening the language file
                for line in f:
                    (key, val) = line.strip().split("=")  # Splitting each line into key and value
                    language_data[key] = val  # Storing key-value pairs in dictionary
                    
        except FileNotFoundError:
            raise ValueError("file not exist")  # Raising error if file not found
        
        return language_data  # Returning the loaded data
    
    @staticmethod
    def get_language_name(language_code):
        language_file = f"data_{language_code}.lng"  # Constructing file name
        try:
            with open(language_file, encoding="utf-8") as f:  # Opening the language file
                for line in f:
                    (key, val) = line.strip().split("=")  # Splitting each line into key and value
                    if key == "language":
                        return val  # Returning the language name
                    
                raise ValueError("Language key not found")  # Raising error if language key not found
        except FileNotFoundError:
            raise ValueError("Language file not found")  # Raising error if file not found
        
app = AddNewGrade()