# 📸 Smart Attendance System

A face recognition-based attendance management system built with Python, OpenCV, and Flask.

## ✨ Features

- **Face Recognition**: Automatically identifies and marks attendance using webcam
- **Real-time Detection**: Instant face detection and recognition
- **Web Dashboard**: View attendance records through a clean web interface
- **MySQL Integration**: Persistent storage of attendance data
- **CSV Export**: Attendance also saved to CSV for easy access

## 🛠️ Tech Stack

- **Python 3.x**
- **OpenCV** - Computer vision and webcam capture
- **face_recognition** - Face detection and recognition
- **Flask** - Web framework for dashboard
- **PyMySQL** - MySQL database connectivity
- **dlib** - Machine learning toolkit for face recognition

## 📁 Project Structure

```
Smart_Attendance_System/
├── app.py              # Flask web application
├── camera.py           # Face recognition webcam script
├── encode_faces.py     # Encode faces from dataset
├── database.py         # MySQL database functions
├── attendance.csv      # Attendance records (CSV)
├── encodings.pkl       # Encoded face data
├── dataset/            # Face images for training
│   └── PersonName/
│       ├── img1.jpg
│       └── img2.jpg
├── static/
│   └── style.css       # Web styling
├── templates/
│   ├── index.html      # Home page
│   └── dashboard.html  # Attendance dashboard
└── venv/               # Virtual environment
```

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Rithish4610/Smart_Attendance_System.git
cd Smart_Attendance_System
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Install dependencies
```bash
pip install opencv-python flask pymysql numpy pandas
pip install dlib-bin
pip install face-recognition --no-deps
pip install face-recognition-models Pillow setuptools
```

### 4. Setup MySQL Database
```sql
CREATE DATABASE attendance_db;
USE attendance_db;

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    time DATETIME
);
```

### 5. Configure database credentials
Update the password in `app.py`, `camera.py`, and `database.py`:
```python
password="your_mysql_password"
```

## 📸 Usage

### Step 1: Add Face Images
Create a folder with your name inside `dataset/` and add 5-10 clear face images:
```
dataset/
└── YourName/
    ├── img1.jpg
    ├── img2.jpg
    └── ...
```

### Step 2: Encode Faces
```bash
python encode_faces.py
```

### Step 3: Run Attendance System
```bash
python camera.py
```
- Face the camera to mark attendance
- Press **Enter** to exit

### Step 4: View Dashboard
```bash
python app.py
```
Open http://127.0.0.1:5000 in your browser

## 📊 Screenshots

- **Home Page**: Instructions and navigation
- **Dashboard**: View all attendance records with timestamps

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `face_recognition` installation fails | Install `dlib-bin` first, then `face-recognition --no-deps` |
| MySQL connection error | Check credentials and ensure MySQL service is running |
| Camera not opening | Check if another app is using the webcam |
| `pkg_resources` warning | Install `setuptools` package |

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Rithish**

---

⭐ Star this repo if you found it helpful!
