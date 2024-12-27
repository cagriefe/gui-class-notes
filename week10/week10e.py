# Scrollable frame

import customtkinter as ctk  # Importing customtkinter for custom GUI components

class CTkApp(ctk.CTk):  # Defining a class that inherits from ctk.CTk
    def __init__(self):  # Constructor method
        super().__init__()  # Calling the constructor of the parent class
        self.geometry("300x450")  # Setting the window size
        self.title("Week 10")  # Setting the window title
        self.labels = []  # Initializing an empty list to store labels
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop

    def create_widgets(self):  # Method to create widgets
        self.frame1 = ctk.CTkScrollableFrame(self, label_text="List of Labels")  # Creating a scrollable frame
        self.entry1 = ctk.CTkEntry(self.frame1, placeholder_text="How many label?")  # Creating an entry widget
        self.btn1 = ctk.CTkButton(self.frame1, text="Add labels", command=self.add_labels)  # Creating a button to add labels
        self.btn2 = ctk.CTkButton(self.frame1, text="Remove labels", command=self.remove_labels)  # Creating a button to remove labels

    def create_layout(self):  # Method to create layout
        self.frame1.pack(pady=20, padx=20, fill="both", expand=True)  # Packing the frame with padding
        self.entry1.pack(pady=(10, 0))  # Packing the entry with padding
        self.btn1.pack(pady=(10, 0))  # Packing the add button with padding
        self.btn2.pack(pady=(10, 0))  # Packing the remove button with padding

    def add_labels(self):  # Method to add labels
        list_size = len(self.labels)  # Getting the current number of labels
        how_many = int(self.entry1.get())  # Converting the entry value to an integer
        for i in range(how_many):  # Looping to create the specified number of labels
            self.labels.append(ctk.CTkLabel(self.frame1, text=f"Label {list_size + i + 1}"))  # Creating and adding a new label to the list
            self.labels[list_size + i].pack(pady=(10, 0))  # Packing the new label with padding

        self.frame1.configure(label_text=f"List of Labels ({len(self.labels)})")  # Updating the frame label text with the new count

    def remove_labels(self):  # Method to remove labels
        for l in self.labels:  # Looping through the list of labels
            l.destroy()  # Destroying each label
        self.labels.clear()  # Clearing the list of labels
        self.frame1.configure(label_text="List of Labels")  # Resetting the frame label text

app = CTkApp()  # Creating an instance of CTkApp