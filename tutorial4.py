import numpy as np
import cv2


cap = cv2.VideoCapture(0)  # Open the default camera

while True:
    ret, frame = cap.read()  # Capture a frame from the camera
    width = int(cap.get(3))  # Get the width of the captured frame
    height = int(cap.get(4))  # Get the height of the captured frame

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 5)  # Draw a blue line from the top-left corner to the bottom-right corner
    img = cv2.line(img, (width, 0), (0, height), (0, 255, 0), 5)  # Draw a green line from the top-right corner to the bottom-left corner
   
   # Draw a red rectangle 
    img = cv2.rectangle(img, (50, 50), (200, 200), (0, 0, 255), -1)  

    # Draw a yellow circle
    img = cv2.circle(img, (width//2, height//2), 50, (0, 255, 255), 2)  

    # Draw a text
    font = cv2.FONT_HERSHEY_TRIPLEX
    img = cv2.putText(img, 'Masfiqun', (width//2 - 100, height//2 + 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Camera', img)  # Display the combined image

    if cv2.waitKey(1) == ord('q'):  # Exit the loop when 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()




