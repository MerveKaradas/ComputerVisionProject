import cv2

img = cv2.imread('../face.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('Tespit Edilen Yuz',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
1. scaleFactor:
Tanım: Bu parametre, görüntünün her ardışık ölçeklendirme işleminde ne kadar küçültüleceğini belirler.
scaleFactor, genellikle 1'den büyük bir değerdir. Örneğin, 1.3 değeri, her ölçeklendirme adımında görüntünün %30 oranında küçültüleceğini ifade eder.
Daha düşük bir scaleFactor değeri (örn. 1.1), daha ayrıntılı bir arama sağlar, ancak işlem süresi uzar.
Daha yüksek bir scaleFactor değeri (örn. 1.5), daha hızlı bir arama sağlar, ancak bazı yüzler atlanabilir.

2. minNeighbors:
Tanım: Bir pencereyi (window) yüz olarak kabul etmek için, o pencerenin çevresinde kaç komşu pencereden destek alması gerektiğini belirler.
Bu değer, pozitif bir tam sayıdır. Örneğin, 5 değeri, bir yüzün algılandığına emin olmak için en az 5 komşu pencerenin de bu yüzü tanımlaması gerektiğini ifade eder.
Daha yüksek bir minNeighbors değeri, daha az yanlış pozitif sonuç (yani, yüz olmayan bölgelerin yüz olarak algılanması) sağlar, ancak bazı gerçek yüzlerin atlanmasına neden olabilir.
Daha düşük bir minNeighbors değeri, daha fazla yüz tespiti sağlar, ancak yanlış pozitif oranını artırabilir.
"""
