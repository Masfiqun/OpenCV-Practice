import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # --- RED ---
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    # --- BLUE ---
    lower_blue = np.array([90,150,0])
    upper_blue = np.array([140,255,255])

    # --- GREEN ---
    lower_green = np.array([40,70,70])
    upper_green = np.array([80,255,255])

    # Create masks
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Function to detect and draw
    def detect_color(mask, color_name, box_color):
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area > 500:
                x, y, w, h = cv2.boundingRect(cnt)

                cv2.rectangle(frame, (x,y), (x+w, y+h), box_color, 2)
                cv2.putText(frame, color_name, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, box_color, 2)

    # Detect each color
    detect_color(mask_red, "RED", (0,0,255))
    detect_color(mask_blue, "BLUE", (255,0,0))
    detect_color(mask_green, "GREEN", (0,255,0))

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()