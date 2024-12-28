# Basic ttkbootstrap GUI

import ttkbootstrap as ttk  # Importing ttkbootstrap for themed tkinter widgets

win = ttk.Window(themename="superhero")  # Creating a window with the "superhero" theme
win.geometry("500x500")  # Setting the window size
win.title("Week 11")  # Setting the window title

btn1 = ttk.Button(win, text="Button 1", bootstyle="success")  # Creating a button with "success" style
btn1.pack(padx=15, pady=(30,15))  # Packing the button with padding

btn2 = ttk.Button(win, text="Button 2", bootstyle=("info", "outline"))  # Creating a button with "info" and "outline" styles
btn2.pack(padx=15, pady=15)  # Packing the button with padding

cbtn1 = ttk.Checkbutton(win, text="Check Button", bootstyle="warning-round-toggle")  # Creating a checkbutton with "warning-round-toggle" style
cbtn1.pack(padx=15, pady=15)  # Packing the checkbutton with padding

date_entry = ttk.DateEntry(win, bootstyle="success", width=10)  # Creating a date entry with "success" style
date_entry.pack(padx=15, pady=15)  # Packing the date entry with padding

win.mainloop()  # Starting the main event loop