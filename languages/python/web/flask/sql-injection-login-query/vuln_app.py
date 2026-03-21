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

    # VULNERABLE: пользовательский ввод напрямую вставляется в SQL-запрос
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    result = cursor.execute(query).fetchone()

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