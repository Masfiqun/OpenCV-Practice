import cv2

# Load the image in color mode
img = cv2.imread('assets/test.jpg', cv2.IMREAD_COLOR)

# Resize the image to half of its original size and rotate it 90 degrees clockwise
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('Test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


