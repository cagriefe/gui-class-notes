# Install customtkinter: https://customtkinter.tomschimansky.com/
# Common CTk widgets

import customtkinter as ctk  # Importing customtkinter for custom GUI components

class CTkApp(ctk.CTk):  # Defining a class that inherits from ctk.CTk
    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.geometry("300x450")  # Setting the window size
        self.title("Week 10")  # Setting the window title
        self.rb_value = ctk.IntVar(value=1)  # Creating an IntVar for radio button value
        self.current_appearance = ctk.StringVar(value="Light")  # Creating a StringVar for appearance mode
        ctk.set_appearance_mode(self.current_appearance.get())  # Setting initial appearance mode
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop

    def create_widgets(self):  # Method to create widgets
        self.frame1 = ctk.CTkFrame(self)  # Creating a CTkFrame
        self.lbl1 = ctk.CTkLabel(self.frame1, text="Label")  # Creating a CTkLabel
        self.entry1 = ctk.CTkEntry(self.frame1, placeholder_text="Type your message.")  # Creating a CTkEntry
        self.combo1 = ctk.CTkComboBox(self.frame1, values=["Item 1", "Item 2", "Item 3"])  # Creating a CTkComboBox
        self.opt_menu1 = ctk.CTkOptionMenu(self.frame1, values=["Item 1", "Item 2", "Item 3"])  # Creating a CTkOptionMenu
        self.chk1 = ctk.CTkCheckBox(self.frame1, text="Checkbox", onvalue="checked", offvalue="unchecked")  # Creating a CTkCheckBox
        self.radio1 = ctk.CTkRadioButton(self.frame1, text="Item 1", variable=self.rb_value, value=1)  # Creating a CTkRadioButton
        self.radio2 = ctk.CTkRadioButton(self.frame1, text="Item 2", variable=self.rb_value, value=2)  # Creating a CTkRadioButton
        self.btn1 = ctk.CTkButton(self.frame1, text="Button", command=self.button_click)  # Creating a CTkButton
        self.progress1 = ctk.CTkProgressBar(self.frame1)  # Creating a CTkProgressBar
        self.slider1 = ctk.CTkSlider(self.frame1, from_=0, to=1, command=self.get_slider_value)  # Creating a CTkSlider
        self.switch1 = ctk.CTkSwitch(self.frame1, textvariable=self.current_appearance, command=self.change_appearance)  # Creating a CTkSwitch

        self.progress1.set(0.8)  # Setting initial value for progress bar
        self.slider1.set(0.8)  # Setting initial value for slider

        self.entry1.bind("<KeyRelease>", self.set_text)  # Binding key release event to set_text method

    def create_layout(self):  # Method to create layout
        self.frame1.pack(pady=20, padx=20, fill="both", expand=True)  # Packing the frame
        self.lbl1.pack(pady=(10, 0))  # Packing the label with padding
        self.entry1.pack(pady=(10, 0))  # Packing the entry with padding
        self.combo1.pack(pady=(10, 0))  # Packing the combo box with padding
        self.opt_menu1.pack(pady=(10, 0))  # Packing the option menu with padding
        self.chk1.pack(pady=(10, 0))  # Packing the checkbox with padding
        self.radio1.pack(pady=(10, 0))  # Packing the first radio button with padding
        self.radio2.pack(pady=(10, 0))  # Packing the second radio button with padding
        self.btn1.pack(pady=(10, 0))  # Packing the button with padding
        self.progress1.pack(pady=(10, 0))  # Packing the progress bar with padding
        self.slider1.pack(pady=(10, 0))  # Packing the slider with padding
        self.switch1.pack(pady=(10, 0))  # Packing the switch with padding

    def set_text(self, event):  # Method to set text of the label
        self.lbl1.configure(text=self.entry1.get())  # Setting label text to entry text

    def button_click(self):  # Method to handle button click
        self.lbl1.configure(text=f"Combobox value is {self.combo1.get()}.\n"
                                 f"Option menu value is {self.opt_menu1.get()}.\n"
                                 f"Checkbox is {self.chk1.get()}.\n"
                                 f"Radio button value is {self.rb_value.get()}.")  # Setting label text with widget values
        print(self.rb_value.get())  # Printing radio button value

    def get_slider_value(self, value):  # Method to get slider value
        self.progress1.set(value)  # Setting progress bar value to slider value
        self.lbl1.configure(text=f"Slider value: {value}")  # Setting label text to slider value

    def change_appearance(self):  # Method to change appearance mode
        if self.current_appearance.get() == "Dark":  # Checking if current mode is Dark
            self.current_appearance.set("Light")  # Setting appearance mode to Light
        else:
            self.current_appearance.set("Dark")  # Setting appearance mode to Dark

        ctk.set_appearance_mode(self.current_appearance.get())  # Applying the appearance mode

app = CTkApp()  # Creating an instance of CTkApp