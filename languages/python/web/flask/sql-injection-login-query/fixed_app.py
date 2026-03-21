from flask import Flask, request
import sqlite3

app = Flask(__name__)

DATABASE = "users.db"


@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # FIX: параметризованный SQL-запрос предотвращает внедрение SQL-кода
    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    result = cursor.execute(query, (username, password)).fetchone()

    conn.close()

    if result:
        return "Login successful"
    else:
        return "Invalid credentials"


@app.route("/")
def index():
    return "Flask Login Demo"


if __name__ == "__main__":
    app.run(debug=True)