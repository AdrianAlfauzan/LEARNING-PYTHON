import sqlite3
import os
os.system("cls")
# Connect to a SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Insert some data into the table
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('Testing1', 'Adrian@gmail.com'))
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('Testing2', 'kaka@gmail.com'))

# Commit the changes
conn.commit()

# Query the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
conn.close()
