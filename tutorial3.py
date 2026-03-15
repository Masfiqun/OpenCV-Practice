import numpy as np
import cv2

# # Just to load the image and display it
# cap = cv2.VideoCapture(0)  # Open the default camera

# while True:
#     ret, frame = cap.read()  # Capture a frame from the camera

#     cv2.imshow('Camera', frame)  # Display the combined image

#     if cv2.waitKey(1) == ord('q'):  # Exit the loop when 'q' is pressed
#         break

# cap.release()
# cv2.destroyAllWindows()




# Create a black image and place the captured frame in the corners

cap = cv2.VideoCapture(0)  # Open the default camera

while True:
    ret, frame = cap.read()  # Capture a frame from the camera
    width = int(cap.get(3))  # Get the width of the captured frame
    height = int(cap.get(4))  # Get the height of the captured frame
    
    image = np.zeros(frame.shape, dtype=np.uint8)  # Create a black image with the same dimensions as the captured frame
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # Resize the captured frame to half its original size
    image[0:height//2, 0:width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Place the smaller frame in the top-left corner of the black image
    image[height//2:, width//2:] = smaller_frame  # Place the smaller frame in the bottom-right corner of the black image
    image[0:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Place the smaller frame in the top-right corner of the black image
    image[height//2:, 0:width//2] = smaller_frame #Place the smaller frame in the bottom-left corner of the black image

    cv2.imshow('Camera', image)  # Display the combined image

    if cv2.waitKey(1) == ord('q'):  # Exit the loop when 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()




