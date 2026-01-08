import cv2
import face_recognition
import pickle
import datetime
import csv
import pymysql

# Database connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Rithish@2007",
    database="attendance_db"
)
cursor = db.cursor()

with open("encodings.pkl", "rb") as f:
    known_encodings, known_names = pickle.load(f)

video = cv2.VideoCapture(0)
marked = set()

while True:
    ret, frame = video.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for encoding, location in zip(encodings, faces):
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"

        if True in matches:
            name = known_names[matches.index(True)]
            if name not in marked:
                marked.add(name)
                now = datetime.datetime.now()
                # Save to CSV
                with open("attendance.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([name, now])
                # Save to MySQL
                sql = "INSERT INTO attendance (name, time) VALUES (%s, %s)"
                cursor.execute(sql, (name, now))
                db.commit()
                print(f"✅ Attendance marked for {name}")

        top, right, bottom, left = location
        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) == 13:  # Enter key
        break

video.release()
cv2.destroyAllWindows()
db.close()
