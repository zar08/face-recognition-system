import cv2 
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'resources'
images = []
class_names = []
my_list = os.listdir(path)
#print(my_list)
for cls in my_list:
    current_image = cv2.imread(f'{path}/{cls}')
    images.append(current_image)
    class_names.append(os.path.splitext(cls)[0])
#print(class_names)

def find_encodings(images):
    encode_list = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(image)[0]
        encode_list.append(encode)
    return encode_list

def mark_attendance(name):
    with open('Attendance.csv', 'r+') as f:
        my_data_list = f.readline()
        name_list = []
        for line in my_data_list:
            entry = line.split(',')
            name_list.append(entry[0])
        if name not in name_list:
            now = datetime.now()
            date_time_string = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {date_time_string}')

encode_list_known = find_encodings(images)
print("Encoding Complete")

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    image_small = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    image_small = cv2.cvtColor(image_small, cv2.COLOR_BGR2RGB)

    faces_current_frame = face_recognition.face_locations(image_small)
    encodes_current_frame = face_recognition.face_encodings(image_small, faces_current_frame)

    for encode_face, face_loc in zip(encodes_current_frame, faces_current_frame):
        matches = face_recognition.compare_faces(encode_list_known, encode_face)
        face_dis = face_recognition.face_distance(encode_list_known, encode_face)
        #print(face_dis)
        match_index = np.argmin(face_dis)

        if matches[match_index]:
            name = class_names[match_index].title()
            #print(name)
            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4 
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            mark_attendance(name)

     # Stop if escape key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.imshow('webcam', frame)
    cv2.waitKey(1)