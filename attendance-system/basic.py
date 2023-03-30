import cv2
import numpy as np
import face_recognition

duterte = face_recognition.load_image_file("resources/duterte.jpg")
duterte = cv2.cvtColor(duterte, cv2.COLOR_BGR2RGB)
test_duterte = face_recognition.load_image_file("resources/test_duterte.jpg")
test_duterte = cv2.cvtColor(test_duterte, cv2.COLOR_BGR2RGB)


# Gives a tuple 
face_location = face_recognition.face_locations(duterte)[0]
encode_duterte = face_recognition.face_encodings(duterte)[0]
cv2.rectangle(duterte, (face_location[3], face_location[0]), (face_location[1], face_location[2]), (50, 205, 50), 2)

face_location_test = face_recognition.face_locations(test_duterte)[0]
encode_duterte_test = face_recognition.face_encodings(test_duterte)[0]
cv2.rectangle(test_duterte, (face_location_test[3], face_location_test[0]), (face_location_test[1], face_location_test[2]), (50, 205, 50), 2)

results = face_recognition.compare_faces([encode_duterte], encode_duterte_test)
face_distance = face_recognition.face_distance([encode_duterte], encode_duterte_test)
#print(results, face_distance)
#cv2.rectangle(test_duterte, f'{results} {round(face_distance[0], 2)}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Duterte", duterte)
cv2.imshow("Test Duterte", test_duterte)

cv2.waitKey(7000)