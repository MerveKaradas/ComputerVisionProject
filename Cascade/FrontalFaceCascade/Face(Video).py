import cv2

cap = cv2.VideoCapture("../people.mp4")
cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

while(True):
    ret, frame = cap.read()

    if ret == False:
        break

    frame = cv2.resize(frame, (500, 600))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(gray, 1.4, 1)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()