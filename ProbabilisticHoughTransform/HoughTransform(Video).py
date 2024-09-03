import numpy as np
import cv2

cap = cv2.VideoCapture("bisikletyolu.mp4")


while True:
    ret, frame = cap.read()

    if ret == False:
        break

    frame = cv2.resize(frame, (500, 550))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    alt = np.array([0, 0, 200])
    ust = np.array([180, 25, 255])

    mask = cv2.inRange(hsv, alt, ust)
    edges = cv2.Canny(mask, 90, 110)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50,500,5,5)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('Cizgiler', frame)

    if cv2.waitKey(24) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()