import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="Rithish@2007",
    database="attendance_db"
)

cursor = db.cursor()

def insert(name, time):
    sql = "INSERT INTO attendance (name, time) VALUES (%s, %s)"
    cursor.execute(sql, (name, time))
    db.commit()
