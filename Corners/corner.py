import cv2
import numpy as np

img = cv2.imread('geo.png')
cv2.imshow('Orjinal Resim',img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Shi-Tomasi köşe tespiti algoritması köşe noktaları bulur
corners = cv2.goodFeaturesToTrack(gray,maxCorners=100, qualityLevel=0.01, minDistance=8)
corners=np.int32(corners) #Tespit edilen köşe noktalarının koordinatlarını tam sayı türüne dönüştürür

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y), 3,200,-1)  #bulunan köşe noktalarına çember çizer (-1 çemberin dolu olmasını sağlar)

cv2.imshow('Tespit Edilen Köseler ',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
