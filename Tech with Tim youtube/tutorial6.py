import numpy as np
import cv2

# This code detects corners in an image and draws lines between them

img = cv2.imread('assets/chess.png')  # Read the image from the file
img = cv2.resize(img, (400, 400))  # Resize the image to 400x400 pixels
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)  # Detect corners in the image
corners = np.int8(corners)  # Convert the corner coordinates to integers

for corner in corners:
    x, y = corner.ravel()  # Get the x and y coordinates of the corner
    cv2.circle(img, (x, y), 5, (0, 255, 0), -1)  # Draw a green circle at the corner location

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))  # Generate a random color
        cv2.line(img, corner1, corner2, color, 1)  # Draw a line between the two corners

cv2.imshow('frame', img)  # Display the original image

cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all windows