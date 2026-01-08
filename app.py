from flask import Flask, render_template
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    password="Rithish@2007",
    database="attendance_db"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM attendance")
    data = cursor.fetchall()
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
