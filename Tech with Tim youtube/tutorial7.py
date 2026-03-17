import numpy as np
import cv2

# This code detects faces and eyes in a video stream from the camera and draws rectangles around them.

cap = cv2.VideoCapture(0)  # Open the default camera
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  # Load the Haar cascade for face detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')  # Load the Haar cascade for eye detection


while True:
    ret, frame = cap.read()  # Read a frame from the camera

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect faces in the frame

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draw a rectangle around each face
        roi_gray = gray[y:y+h, x:x+w]  # Extract the region of interest (ROI) for the face
        roi_color = frame[y:y+h, x:x+w]  # Extract the color ROI for the face
        eyes = eye_cascade.detectMultiScale(roi_gray)  # Detect eyes in the face ROI
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)  # Draw a rectangle around each eye


    cv2.imshow('frame', frame)  # Display the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for the 'q' key to be pressed
        break  # Exit the loop

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all windows