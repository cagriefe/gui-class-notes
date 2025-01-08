# Import the customtkinter module as ctk
import customtkinter as ctk

# Define a class UnitConverter that inherits from ctk.CTk
class UnitConverter(ctk.CTk):
    
    # Initialize the UnitConverter class
    def __init__(self):
       super().__init__()
       self.geometry("310x200")
       ctk.set_default_color_theme("blue")
       ctk.set_appearance_mode("light")
       self.title("Unit Converter")
       self.resizable(False,False)
       self.create_widgets()
       self.create_layout()
       self.mainloop()
    
    # Method to create widgets
    def create_widgets(self):
        self.container = ctk.CTkFrame(self)
        self.lbl_entry = ctk.CTkLabel(self.container, text="Enter value:")
        self.lbl_combo = ctk.CTkLabel(self.container, text="Convert")
        self.lbl_result = ctk.CTkLabel(self.container, text="Enter a number and click the convert button.")
        
        self.txt_entry = ctk.CTkEntry(self.container,)
        self.cmb_unit = ctk.CTkComboBox(self.container, values=["Miles to Kilometer", "Kilometer to miles"])
        
        self.btn_convert = ctk.CTkButton(self.container, text="Convert", width=80, command=self.convert)
        self.bind("<Return>", lambda e : self.convert())
        
    # Method to create the layout
    def create_layout(self):
        self.container.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.container.columnconfigure(index=0, weight=1)
        self.container.columnconfigure(index=1, weight=2)
        
        self.container.rowconfigure(index=0, weight=1)
        self.container.rowconfigure(index=1, weight=1)
        self.container.rowconfigure(index=2, weight=1)
        self.container.rowconfigure(index=3, weight=1)
        
        self.lbl_entry.grid(row=0, column=0, padx=10, pady=10)
        self.txt_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")
        self.lbl_combo.grid(row=1, column=0, padx=10, pady=10)
        self.cmb_unit.grid(row=1, column=1, padx=10, pady=10, sticky="we")
        self.btn_convert.grid(row=2, column=1, padx=10, pady=10, sticky="e")
        self.lbl_result.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
    # Method to perform the conversion
    def convert(self):
        try:
            value = float(self.txt_entry.get())
            if self.cmb_unit.get() == "Miles to Kilometer":
                result = value * 1.60934
                self.lbl_result.configure(text=f"{result:.2f} Kilometers")
            elif self.cmb_unit.get() == "Kilometer to miles":
                result = value / 1.60934
                self.lbl_result.configure(text=f"{result:.2f} Miles")
        except ValueError:
            self.lbl_result.configure(text="Invalid input please enter a number")
        
# Create an instance of the UnitConverter class and run the application
app = UnitConverter()