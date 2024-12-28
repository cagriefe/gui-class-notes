import sqlite3  # Importing sqlite3 for database operations

class ToDoDatabase:

    def __init__(self, db_name="todo_list.db"):  # Constructor method
        self.db_name = db_name  # Setting the database name

    def create_table(self):  # Method to create the table
        conn = sqlite3.connect(self.db_name)  # Connecting to the database
        cur = conn.cursor()  # Creating a cursor object
        cur.execute("""
            create table if not exists todolist (
                id integer primary key autoincrement,
                item text not null,
                status text default 'Pending'
            );
        """)  # Creating the table if it doesn't exist
        conn.commit()  # Committing the transaction
        conn.close()  # Closing the connection

    def add_item(self, item):  # Method to add an item
        conn = sqlite3.connect(self.db_name)  # Connecting to the database
        cur = conn.cursor()  # Creating a cursor object
        cur.execute("insert into todolist (item) values (?)", (item,))  # Inserting the item into the table
        conn.commit()  # Committing the transaction
        conn.close()  # Closing the connection

    def get_items(self):  # Method to get all items
        conn = sqlite3.connect(self.db_name)  # Connecting to the database
        cur = conn.cursor()  # Creating a cursor object
        cur.execute("select id, item, status from todolist")  # Selecting all items from the table
        items = cur.fetchall()  # Fetching all results
        conn.close()  # Closing the connection

        return items  # Returning the items

    def delete_item(self, item_id):  # Method to delete an item
        conn = sqlite3.connect(self.db_name)  # Connecting to the database
        cur = conn.cursor()  # Creating a cursor object
        cur.execute("delete from todolist where id = ?", (item_id,))  # Deleting the item with the given id
        conn.commit()  # Committing the transaction
        conn.close()  # Closing the connection

    def update_status(self, item_id, status):  # Method to update the status of an item
        conn = sqlite3.connect(self.db_name)  # Connecting to the database
        cur = conn.cursor()  # Creating a cursor object
        cur.execute("update todolist set status = ? where id = ?", (status, item_id))  # Updating the status of the item with the given id
        conn.commit()  # Committing the transaction
        conn.close()  # Closing the connection