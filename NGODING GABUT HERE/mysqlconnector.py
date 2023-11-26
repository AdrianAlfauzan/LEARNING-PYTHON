import mysql.connector
import sqlite3
import os

# Clear the console screen
os.system("cls")

# Connect to SQLite database
conn_sqlite = sqlite3.connect('example.db')
cursor_sqlite = conn_sqlite.cursor()

# Create SQLite table if not exists
cursor_sqlite.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Insert some data into the SQLite table
cursor_sqlite.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('Testing1', 'Adrian@gmail.com'))
cursor_sqlite.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('Testing2', 'kaka@gmail.com'))

# Commit the changes to SQLite
conn_sqlite.commit()

# Query data from SQLite
cursor_sqlite.execute("SELECT * FROM users")
rows_sqlite = cursor_sqlite.fetchall()

# Connect to MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Database_Python'
)
cursor_mysql = db.cursor()

# Create MySQL table if not exists
cursor_mysql.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
''')

# Insert data into MySQL from SQLite
for row in rows_sqlite:
   cursor_mysql.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (row[1], row[2]))


# Commit the changes to MySQL
db.commit()

# Query the data from MySQL
cursor_mysql.execute("SELECT * FROM users")
rows_mysql = cursor_mysql.fetchall()

# Print the data from MySQL
for row in rows_mysql:
    print(row)

# Close the connections
conn_sqlite.close()
db.close()
