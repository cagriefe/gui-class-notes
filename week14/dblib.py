import sqlite3

class ToDoDatabase:

    def __init__(self, db_name="todo_list.db"):
        self.db_name = db_name

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("""
            create table if not exists todolist (
                id integer primary key autoincrement,
                item text not null,
                status text default 'Pending'
            );
        """)
        conn.commit()
        conn.close()

    def add_item(self, item):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("insert into todolist (item) values (?)", (item,))
        conn.commit()
        conn.close()

    def get_items(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("select id, item, status from todolist")
        items = cur.fetchall()
        conn.close()

        return items

    def delete_item(self, item_id):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("delete from todolist where id = ?", (item_id,))
        conn.commit()
        conn.close()

    def update_status(self, item_id, status):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("update todolist set status = ? where id = ?", (status, item_id))
        conn.commit()
        conn.close()