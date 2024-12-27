# Textbox, segmented button, and tab view widgets

import customtkinter as ctk  # Importing customtkinter for custom GUI components

class CTkApp(ctk.CTk):  # Defining a class that inherits from ctk.CTk
    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.geometry("300x450")  # Setting the window size
        self.title("Week 10")  # Setting the window title
        self.sb_value = ctk.StringVar(value="Option 3")  # Creating a StringVar for segmented button value
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop

    def create_widgets(self):  # Method to create widgets
        self.frame1 = ctk.CTkFrame(self)  # Creating a CTkFrame
        self.textbox1 = ctk.CTkTextbox(self.frame1, wrap="none", width=240, height=80)  # Creating a CTkTextbox
        self.segmented_btn1 = ctk.CTkSegmentedButton(self.frame1, values=["Option 1", "Option 2", "Option 3"], variable=self.sb_value, command=self.sb_selection)  # Creating a CTkSegmentedButton
        self.tabview1 = ctk.CTkTabview(self.frame1, anchor="sw")  # Creating a CTkTabview, anchor sets the placement of the segmented tab buttons
        self.tab1 = self.tabview1.add("Tab 1")  # Adding Tab 1 to the tab view
        self.tab2 = self.tabview1.add("Tab 2")  # Adding Tab 2 to the tab view
        self.tabview1.set("Tab 2")  # Setting the default tab to Tab 2
        self.lbl1 = ctk.CTkLabel(self.tab1, text="This is tab 1.")  # Creating a CTkLabel for Tab 1
        self.lbl2 = ctk.CTkLabel(self.tab2, text="This is tab 2.")  # Creating a CTkLabel for Tab 2
        self.btn1 = ctk.CTkButton(self.tab2, text="Exit", command=lambda: self.destroy())  # Creating a CTkButton to exit the application

    def create_layout(self):  # Method to create layout
        self.frame1.pack(pady=20, padx=20, fill="both", expand=True)  # Packing the frame
        self.textbox1.pack(pady=(10, 0))  # Packing the textbox with padding
        self.segmented_btn1.pack(pady=(10, 0))  # Packing the segmented button with padding
        self.tabview1.pack(padx=10, pady=10)  # Packing the tab view with padding
        self.lbl1.pack(pady=(30, 0))  # Packing the label in Tab 1 with padding
        self.lbl2.pack(pady=(30, 0))  # Packing the label in Tab 2 with padding
        self.btn1.pack(pady=(30, 0))  # Packing the button in Tab 2 with padding

    def sb_selection(self, value):  # Method to handle segmented button selection
        self.textbox1.insert("end", f"{value} selected.\n")  # Inserting selected value into the textbox
        self.textbox1.see("end")  # Scrolling to the end of the textbox

app = CTkApp()  # Creating an instance of CTkApp