
import cv2

img = cv2.imread("../face.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cascade_face =cv2.CascadeClassifier("../haarcascade_frontalface_default.xml")
cascade_eye  = cv2.CascadeClassifier("../haarcascade_eye.xml")

faces = cascade_face.detectMultiScale(gray,1.3,4)


for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    img2=img[y:y+h,x:x+w]
    gray2=gray[y:y+h,x:x+w]

    eyes = cascade_eye.detectMultiScale(gray2, 1.3, 4)

    for (x1,y1,w1,h1) in eyes:
        cv2.rectangle(img2,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)



cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
