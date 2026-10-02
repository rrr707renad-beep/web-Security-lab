from flask import Flask, render_template, request
app = Flask(__name__)
from werkzeug.security import check_password_hash
import sqlite3
@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT PASSWORD FROM users WHERE username = ?", 
            (username,)    
        )
        user = cursor.fetchone()
        connection.close()
        if user and check_password_hash(user[0], password):
            message = "Login successful!"
        else:
            message = "Invalid username or password."
    return render_template("login.html", message=message)
    if __name__ == "__main__":
        app.run(debug=True)
        