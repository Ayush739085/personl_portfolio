from flask import Flask, render_template, redirect, url_for, session, request
import sqlite3
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")

def get_db():
    conn = sqlite3.connect("portfolio.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        message TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        github TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notifications(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------------- Routes ----------------

@app.route("/")
def home():
    return render_template("intro.html")

@app.route("/landing")
def landing():
    return render_template("landing.html")

@app.route("/dashboard")
def dashboard():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects_data = cursor.fetchall()
    conn.close()
    return render_template("dashboard.html", projects=projects_data)

@app.route("/portfolio")
def portfolio():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects_data = cursor.fetchall()
    conn.close()
    return render_template("portfolio.html", projects=projects_data)

@app.route("/ai-tools")
def ai_tools():
    return render_template("ai_tools.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts(name,email,message) VALUES(?,?,?)",
        (name, email, message)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("dashboard"))

@app.route("/admin-login", methods=["GET","POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "12345":
            return redirect(url_for("admin"))
        return "Invalid Username or Password"
    return render_template("admin_login.html")

@app.route("/admin")
def admin():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM projects")
    total_projects = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM contacts")
    total_messages = cursor.fetchone()[0]
    conn.close()
    return render_template(
        "admin_dashboard.html",
        total_projects=total_projects,
        total_messages=total_messages
    )

@app.route("/messages")
def messages():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()
    conn.close()
    return render_template("messages.html", messages=data)

@app.route("/add-project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        github = request.form["github"]

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO projects(title, description, github) VALUES (?, ?, ?)",
            (title, description, github)
        )
        cursor.execute(
            "INSERT INTO notifications(text) VALUES(?)",
            ("New Project Added",)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("admin"))

    return render_template("add_project.html")

@app.route("/projects")
def projects():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    data = cursor.fetchall()
    conn.close()
    return render_template("projects.html", projects=data)

@app.route("/delete-project/<int:id>")
def delete_project(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("projects"))

if __name__ == "__main__":
    app.run(debug=True)