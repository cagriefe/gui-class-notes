# Run database_setup.py first.

import ttkbootstrap as ttk  # Importing ttkbootstrap for themed tkinter widgets
import dblib  # Importing dblib for database operations

class ToDoList(ttk.Window):  # Defining a class that inherits from ttk.Window
    def __init__(self):  # Constructor method
        super().__init__(themename="litera")  # Calling the constructor of the parent class with a theme
        self.geometry("600x720")  # Setting the window size
        self.title("To-Do List App")  # Setting the window title
        self.db = dblib.ToDoDatabase()  # Creating an instance of the database
        self.status_var = ttk.IntVar()  # Creating an IntVar for the status checkbutton
        self.create_widgets()  # Calling method to create widgets
        self.create_layout()  # Calling method to create layout
        self.mainloop()  # Starting the main event loop

    def create_widgets(self):  # Method to create widgets
        # Widgets for adding new To-Do items
        self.frm_add = ttk.Labelframe(self, text="Add To-Do Item")  # Creating a Labelframe for adding items
        self.entry_item = ttk.Entry(self.frm_add)  # Creating an entry widget for the item
        self.btn_add = ttk.Button(self.frm_add, text="Add", command=self.add_item)  # Creating a button to add the item

        # Widgets for listing To-Do items
        self.frm_list = ttk.Labelframe(self, text="To-Do List")  # Creating a Labelframe for the list
        self.tv = ttk.Treeview(self.frm_list, columns=("Item", "Status"), show="headings", selectmode="browse")  # Creating a Treeview widget
        self.tv.heading("Item", text="Item")  # Setting the heading for the Item column
        self.tv.heading("Status", text="Status")  # Setting the heading for the Status column

        # Widgets for deleting/updating To-Do items
        self.frm_actions = ttk.Labelframe(self, text="Actions")  # Creating a Labelframe for actions
        self.btn_delete = ttk.Button(self.frm_actions, text="Delete", command=self.delete_item)  # Creating a button to delete the item
        self.cbtn_status = ttk.Checkbutton(self.frm_actions, text="Mark as Completed", variable=self.status_var, command=self.toggle_status, bootstyle="round-toggle")  # Creating a checkbutton to mark the item as completed

        # Event bindings for the Treeview and Entry widgets
        self.tv.bind("<<TreeviewSelect>>", self.on_item_select)  # Binding the Treeview selection event
        self.entry_item.bind("<Return>", lambda e : self.add_item())  # Binding the Return key to the add_item method

        # Populate the Treeview
        self.refresh_list()  # Calling method to populate the Treeview

    def create_layout(self):  # Method to create layout
        # Place Labelframe widgets
        self.frm_add.pack(fill="x", padx=15, pady=(15, 0))  # Packing the add item frame with padding
        self.frm_list.pack(fill="both", expand=True, padx=15, pady=(15, 0))  # Packing the list frame with padding
        self.frm_actions.pack(fill="x", padx=15, pady=15)  # Packing the actions frame with padding

        # Place entry and add button widgets
        self.entry_item.pack(side="left", padx=(15, 0), pady=15, fill="x", expand=True)  # Packing the entry widget with padding
        self.btn_add.pack(side="right", padx=15, pady=15)  # Packing the add button with padding

        # Place the Treeview widget
        self.tv.pack(fill="both", expand=True, padx=15, pady=15)  # Packing the Treeview with padding

        # Place delete button and status checkbutton widgets
        self.btn_delete.pack(side="left", padx=15, pady=15)  # Packing the delete button with padding
        self.cbtn_status.pack(side="right", padx=15, pady=15)  # Packing the status checkbutton with padding

    def enable_actions(self):  # Method to enable action buttons
        self.btn_delete.configure(state="normal")  # Enabling the delete button
        self.cbtn_status.configure(state="normal")  # Enabling the status checkbutton

    def disable_actions(self):  # Method to disable action buttons
        self.btn_delete.configure(state="disabled")  # Disabling the delete button
        self.cbtn_status.configure(state="disabled")  # Disabling the status checkbutton

    def on_item_select(self, event):  # Method to handle item selection
        selected_item = self.tv.selection()  # Getting the selected item
        if selected_item:  # If an item is selected
            item_id = int(selected_item[0])  # Getting the item ID
            item_status = self.tv.item(item_id)["values"][1]  # Getting the item status
            if item_status == "Done":  # If the item is marked as done
                self.status_var.set(1)  # Setting the checkbutton to checked
            else:  # If the item is not marked as done
                self.status_var.set(0)  # Setting the checkbutton to unchecked

    def refresh_list(self):  # Method to refresh the list
        for item in self.tv.get_children():  # Clearing the Treeview content
            self.tv.delete(item)  # Deleting each item

        for row in self.db.get_items():  # Fetching updated data and populating the Treeview
            self.tv.insert(parent="", index="end", iid=row[0], values=(row[1], row[2]))  # Inserting each row

        tv_items = self.tv.get_children()  # Getting the Treeview items
        if tv_items:  # If there are items in the Treeview
            self.enable_actions()  # Enabling the action buttons
            self.tv.selection_set(tv_items[-1])  # Selecting the last item
        else:  # If there are no items in the Treeview
            self.disable_actions()  # Disabling the action buttons

    def add_item(self):  # Method to add an item
        item = self.entry_item.get().strip()  # Getting the item from the entry widget
        if item:  # If the item is not empty
            self.db.add_item(item)  # Adding the item to the database
            self.refresh_list()  # Refreshing the list
            self.entry_item.delete(0, "end")  # Clearing the entry widget
            self.entry_item.focus_set()  # Setting focus to the entry widget

    def delete_item(self):  # Method to delete an item
        selected_item = self.tv.selection()  # Getting the selected item
        if selected_item:  # If an item is selected
            item_id = int(selected_item[0])  # Getting the item ID
            self.db.delete_item(item_id)  # Deleting the item from the database
            self.refresh_list()  # Refreshing the list

    def toggle_status(self):  # Method to toggle the status of an item
        selected_item = self.tv.selection()  # Getting the selected item
        if selected_item:  # If an item is selected
            item_id = int(selected_item[0])  # Getting the item ID
            if self.status_var.get() == 1:  # If the checkbutton is checked
                new_status = "Done"  # Setting the new status to Done
            else:  # If the checkbutton is unchecked
                new_status = "Pending"  # Setting the new status to Pending
            self.db.update_status(item_id, new_status)  # Updating the status in the database
            self.refresh_list()  # Refreshing the list
            self.tv.selection_set(selected_item)  # Keeping the current item selected

app = ToDoList()  # Creating an instance of ToDoList