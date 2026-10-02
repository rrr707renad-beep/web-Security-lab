import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

password_hash = generate_password_hash("Test123!")

cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ("testuser", password_hash)
)

connection.commit()
connection.close()

print("User created successfully!")