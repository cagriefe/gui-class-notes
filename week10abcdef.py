# Import the customtkinter module as ctk
import customtkinter as ctk

# Define a class UnitConverter that inherits from ctk.CTk
class UnitConverter(ctk.CTk):
    
    # Initialize the UnitConverter class
    def __init__(self):
        super().__init__()  # Call the parent class (ctk.CTk) constructor
        ctk.set_default_color_theme("blue")  # Set the default color theme to blue
        ctk.set_appearance_mode("light")  # Set the appearance mode to light
        self.geometry("310x200")  # Set the window size to 310x200 pixels
        self.title("Unit Converter")  # Set the window title to "Unit Converter"
        self.resizable(False, False)  # Make the window non-resizable
        self.create_widgets()  # Call the method to create widgets
        self.create_layout()  # Call the method to create the layout
        self.mainloop()  # Start the main event loop
        
    # Method to create widgets
    def create_widgets(self):
        self.container = ctk.CTkFrame(self)  # Create a frame to contain other widgets
        self.lbl_entry = ctk.CTkLabel(self.container, text="Enter value:")  # Label for entry
        self.lbl_combo = ctk.CTkLabel(self.container, text="Convert")  # Label for combo box
        self.lbl_result = ctk.CTkLabel(self.container, text="Enter a number and click the Convert button.")  # Label for result
        
        self.txt_entry = ctk.CTkEntry(self.container)  # Entry widget for user input
        self.cmb_unit = ctk.CTkComboBox(self.container, values=["Miles to Kilometers", "Kilometers to Miles"])  # Combo box for unit selection
        self.btn_convert = ctk.CTkButton(self.container, text="Convert", width=80, command=self.convert)  # Button to trigger conversion
        
        self.bind("<Return>", lambda e : self.convert())  # Bind the Enter key to the convert method
        
    # Method to create the layout
    def create_layout(self):
        self.container.pack(pady=10, padx=10, fill="both", expand=True)  # Pack the container with padding and expansion
        
        # Configure the grid layout for the container
        self.container.columnconfigure(index=0, weight=1)
        self.container.columnconfigure(index=1, weight=2)
        
        self.container.rowconfigure(index=0, weight=1)
        self.container.rowconfigure(index=1, weight=1)
        self.container.rowconfigure(index=2, weight=1)
        self.container.rowconfigure(index=3, weight=1)
        
        # Place the widgets in the grid
        self.lbl_entry.grid(row=0, column=0, padx=10, pady=(10,0))
        self.txt_entry.grid(row=0, column=1, padx=10, pady=(10,0), sticky="we")
        self.lbl_combo.grid(row=1, column=0, padx=10, pady=(10,0))
        self.cmb_unit.grid(row=1, column=1, padx=10, pady=(10,0), sticky="we")
        self.btn_convert.grid(row=2, column=1, padx=10, pady=(10,0), sticky="e")
        self.lbl_result.grid(row=3, column=0, padx=10, pady=(10,0), columnspan=2)
        
    # Method to perform the conversion
    def convert(self):
        try:
            value = float(self.txt_entry.get())  # Get the value from the entry widget and convert to float
            if self.cmb_unit.get() == "Miles to Kilometers":  # Check if the selected conversion is Miles to Kilometers
                result = value * 1.60934  # Convert miles to kilometers
                self.lbl_result.configure(text=f"{result:.2f} Kilometers")  # Update the result label with the conversion
            elif self.cmb_unit.get() == "Kilometers to Miles":  # Check if the selected conversion is Kilometers to Miles
                result = value / 1.60934  # Convert kilometers to miles
                self.lbl_result.configure(text=f"{result:.2f} Miles")  # Update the result label with the conversion
        except ValueError:
            self.lbl_result.configure(text="Invalid input. Please enter a number")  # Handle invalid input
            
# Create an instance of the UnitConverter class and run the application
app = UnitConverter()