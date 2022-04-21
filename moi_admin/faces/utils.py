import numpy as np
import cv2
import face_recognition


def get_encodings(bytes_stream):
    file_bytes = np.asarray(bytearray(bytes_stream.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    small_frame = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
    gray_image = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    faces_on_frame = face_recognition.face_locations(gray_image)
    face_encodings = face_recognition.face_encodings(gray_image, faces_on_frame)
    return face_encodings
