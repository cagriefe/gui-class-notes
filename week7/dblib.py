# Database operations

import sqlite3

class GradeBookDatabase:

    def __init__(self, db_name="gradebook.db"):
        self.db_name = db_name  # Set the database name

    def create_table(self):
        # Create the GradeBook table if it doesn't exist
        conn = sqlite3.connect(self.db_name)  # Connect to the database
        cur = conn.cursor()  # Create a cursor object
        cur.execute("""
            create table if not exists GradeBook (
                gid   integer primary key autoincrement,
                fname text,
                lname text,
                grade integer
            );
            """)  # Execute the SQL command to create the table
        conn.commit()  # Commit the changes
        conn.close()  # Close the connection

    def fill_data(self):
        # Fill the GradeBook table with initial data
        conn = sqlite3.connect(self.db_name)  # Connect to the database
        cur = conn.cursor()  # Create a cursor object
        data = [('Melissa', 'Bishop', 70),
                ('Linda', 'Scanlon', 55),
                ('Russel', 'Gruver', 60),
                ('Maria', 'Mayes', 100),
                ('Dennis', 'Hill', 95),
                ('Nathan', 'Martin', 40),
                ('William', 'Biggs', 85),
                ('Lois', 'Ballard', 60),
                ('Larry', 'Manning', 50),
                ('Dustin', 'Smalls', 30),
                ('Alice', 'Lucas', 70),
                ('John', 'Howell', 90)]  # List of initial data

        for item in data:
            cur.execute("insert into GradeBook(fname, lname, grade) values(?, ?, ?)", item)  # Insert each item into the table

        conn.commit()  # Commit the changes
        conn.close()  # Close the connection

    def save_grade(self, fname, lname, grade):
        # Save a new grade to the GradeBook table
        conn = sqlite3.connect(self.db_name)  # Connect to the database
        cur = conn.cursor()  # Create a cursor object
        cur.execute("insert into GradeBook(fname, lname, grade) values(?, ?, ?)", (fname, lname, grade))  # Insert the grade into the table
        conn.commit()  # Commit the changes
        conn.close()  # Close the connection

    def get_grades(self):
        # Retrieve all grades from the GradeBook table
        conn = sqlite3.connect(self.db_name)  # Connect to the database
        cur = conn.cursor()  # Create a cursor object
        cur.execute("select * from GradeBook")  # Execute the SQL command to retrieve all grades
        grade_list = cur.fetchall()  # Fetch all results
        conn.close()  # Close the connection

        return grade_list  # Return the list of grades

    def get_count_and_average(self):
        # Get the count and average of grades from the GradeBook table
        conn = sqlite3.connect(self.db_name)  # Connect to the database
        cur = conn.cursor()  # Create a cursor object
        cur.execute("select count(*), avg(grade) from GradeBook")  # Execute the SQL command to get the count and average
        result = cur.fetchone()  # Fetch the result
        conn.close()  # Close the connection

        return result  # Return the result

    def delete_grade(self, gid):
        # Delete a grade from the GradeBook table by gid
        conn = sqlite3.connect(self.db_name)  # Connect to the database
        cur = conn.cursor()  # Create a cursor object
        cur.execute("delete from GradeBook where gid=?", (gid, ))  # Execute the SQL command to delete the grade
        conn.commit()  # Commit the changes
        conn.close()  # Close the connection