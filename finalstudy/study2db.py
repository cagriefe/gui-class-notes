import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("temperature_history.db")
cursor = conn.cursor()

# Create the 'conversions' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        result TEXT
    )
""")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'temperature_history.db' and table 'conversions' created successfully.")