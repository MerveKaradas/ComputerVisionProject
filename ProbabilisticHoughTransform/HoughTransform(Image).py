import cv2
import numpy as np

img = cv2.imread("labirent.png")
cv2.imshow("Orjinal Resim", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 70, 80, apertureSize=3)
#cv2.Canny(gray, 70, 80, apertureSize=3): Canny kenar algılama algoritmasını kullanarak görüntüdeki kenarları tespit eder.
#70 ve 80: Kenar tespiti için kullanılan eşik değerleridir.
#apertureSize=3: Kullanılan Sobel operatörünün boyutunu belirler (bu durumda 3x3).

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 80, minLineLength=5, maxLineGap=5)
#Hough dönüşümü algoritmasıyla doğrusal çizgileri tespit eder.

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Cizgileri Cikarilmiş Resim', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
cv2.HoughLinesP(edges, 1, np.pi / 180, 80, minLineLength=10, maxLineGap=10): Hough dönüşümü algoritmasıyla doğrusal çizgileri tespit eder.
edges: Kenar tespiti yapılmış görüntü.
1: Hough uzayında piksellerin birim uzunluktaki mesafesi.
np.pi / 180: Hough uzayında piksellerin açısal çözünürlüğü (radyan cinsinden).
80: Bir çizginin tespit edilmesi için gereken minimum oy sayısı (bu eşik değeri artırarak daha belirgin çizgiler tespit edilir).
minLineLength=10: Tespit edilmesi gereken minimum çizgi uzunluğu.
maxLineGap=10: Çizgiler arasında izin verilen maksimum boşluk.
"""