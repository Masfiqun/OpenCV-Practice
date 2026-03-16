import numpy as np
import cv2


cap = cv2.VideoCapture(0)  # Open the default camera

while True:
    ret, frame = cap.read()  # Capture a frame from the camera
    width = int(cap.get(3))  # Get the width of the captured frame
    height = int(cap.get(4))  # Get the height of the captured frame

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame to HSV color space
    lower_blue = np.array([90, 50, 50])  # Define the lower bound for blue color
    upper_blue = np.array([130, 255, 255])  # Define the upper bound for blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)  # Create a mask for the blue color
    result = cv2.bitwise_and(frame, frame, mask=mask)  # Apply the mask to the original frame to get the result

    cv2.imshow('Camera', result)  # Display the combined image
    cv2.imshow('Mask', mask)  # Display the mask

    if cv2.waitKey(1) == ord('q'):  # Exit the loop when 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()