import cv2
import random

# Load the image in color mode
img = cv2.imread('assets/test.jpg', cv2.IMREAD_COLOR)

for i in range(100):
    for j in range(img.shape[1]):
        img[i, j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]  # Set the pixel to a random color

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()