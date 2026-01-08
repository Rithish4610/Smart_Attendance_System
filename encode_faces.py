import face_recognition
import os
import pickle

dataset_path = "dataset"
known_encodings = []
known_names = []

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)
    for img in os.listdir(person_path):
        image = face_recognition.load_image_file(os.path.join(person_path, img))
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(person)

with open("encodings.pkl", "wb") as f:
    pickle.dump((known_encodings, known_names), f)

print("✅ Face Encodings Saved")
