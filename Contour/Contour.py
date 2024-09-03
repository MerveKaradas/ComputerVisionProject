import cv2

img = cv2.imread('hand.png')
cv2.imshow('Orjinal Resim', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Eşik değerlerini değiştirebilirsin ben 120-250 yaptım, THRESH_BINARY ile ikili hale dönüştürdük (0-siyah 1-beyaz)
ret, thresh = cv2.threshold(gray, 120, 250, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
#-1 parametresi resmin her yerindeki konturleri bulurken, 1 parametresi solu 0 parametresi sağ konturleri bulur.

cv2.imshow('Konturlu Resim', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Kontür belirleme, bir görüntüdeki nesnelerin kenarlarını bulmak için kullanılır.
Genellikle, kontür belirleme işlemi bir görüntüdeki nesneleri ayırmak, analiz etmek veya nesne tespiti yapmak için 
kullanılır. Bu işlem genellikle bir eşikleme (thresholding) işlemi ile başlar. Eşikleme, bir görüntüyü ikili (binary) 
bir görüntüye dönüştürerek belirli bir parlaklık seviyesinin üzerindeki pikselleri beyaz (1), altındakileri ise siyah (0) 
yapar.
"""
