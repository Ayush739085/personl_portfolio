from flask import Flask, render_template, redirect, url_for, session, request
import sqlite3

app = Flask(__name__)

app.config["SECRET_KEY"] = "ayush_ai_workspace_2026"

# ---------------- Home ----------------

@app.route("/")
def home():
    return render_template("intro.html")

@app.route("/landing")
def landing():
    return render_template("landing.html")

@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", projects=projects)
@app.route("/portfolio")
def portfolio():

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()

    conn.close()

    return render_template("portfolio.html", projects=projects)

@app.route("/ai-tools")
def ai_tools():
    return render_template("ai_tools.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


# ---------------- Database ----------------

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

conn.commit()
conn.close()

# ---------------- Contact Form ----------------

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts(name,email,message) VALUES(?,?,?)",
        (name,email,message)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))
conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

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

# ---------------- Admin Login ----------------

@app.route("/admin-login", methods=["GET","POST"])
def admin_login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "12345":
            return redirect(url_for("admin"))

        return "Invalid Username or Password"

    return render_template("admin_login.html")


# ---------------- Admin Dashboard ----------------

@app.route("/admin")
def admin():

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    # Total Projects
    cursor.execute("SELECT COUNT(*) FROM projects")
    total_projects = cursor.fetchone()[0]

    # Total Messages
    cursor.execute("SELECT COUNT(*) FROM contacts")
    total_messages = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "admin_dashboard.html",
        total_projects=total_projects,
        total_messages=total_messages
    )


# ---------------- Messages ----------------

# ---------------- Messages ----------------

@app.route("/messages")
def messages():

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()

    conn.close()

    return render_template("messages.html", messages=data)


# ---------------- Add Project ----------------

# ---------------- Add Project ----------------

@app.route("/add-project", methods=["GET", "POST"])
def add_project():

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        github = request.form["github"]

        conn = sqlite3.connect("portfolio.db")
        cursor = conn.cursor()

        # Project Save
        cursor.execute(
            "INSERT INTO projects(title, description, github) VALUES (?, ?, ?)",
            (title, description, github)
        )

        # Notification Save
        cursor.execute(
            "INSERT INTO notifications(text) VALUES(?)",
            ("New Project Added",)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("admin"))

    return render_template("add_project.html")


# ---------------- View Projects ----------------

@app.route("/projects")
def projects():

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects")
    data = cursor.fetchall()
    print(data)

    conn.close()

    return render_template("projects.html", projects=data)

@app.route("/delete-project/<int:id>")
def delete_project(id):

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM projects WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("projects"))
if __name__ == "__main__":
    app.run(debug=True)
