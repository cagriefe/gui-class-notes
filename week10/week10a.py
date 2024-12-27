# Install customtkinter: pip install customtkinter
# Basic CTk GUI

import customtkinter as ctk  # Importing customtkinter for custom GUI components

def change_appearance():  # Function to change appearance mode
    if ctk.get_appearance_mode() == "Dark":  # Checking if current mode is Dark
        ctk.set_appearance_mode("Light")  # Setting appearance mode to Light
    else:
        ctk.set_appearance_mode("Dark")  # Setting appearance mode to Dark

win = ctk.CTk()  # Creating a CTk window
win.title("Week 10")  # Setting the window title
win.geometry("300x200")  # Setting the window size

lbl = ctk.CTkLabel(win, text="GUI Programming with Python", fg_color=("orange", "green"), corner_radius=20)  # Creating a CTkLabel
lbl.pack(pady=20)  # Packing the label with padding

btn = ctk.CTkButton(win, text="Change Appearance", command=change_appearance)  # Creating a CTkButton
btn.pack()  # Packing the button

win.mainloop()  # Starting the main event loop