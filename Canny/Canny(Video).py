import cv2

cap = cv2.VideoCapture(0) # Bilgisayarın birincil kamerasını alma

while True:
    ret, frame = cap.read() # Kameradan goruntü alma

    frame = cv2.flip(frame, 1) # görüntüyü yatay çevirme

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # frameler griye çevrildi

    corners = cv2.Canny(gray, 100, 200)

    cv2.imshow('frame', frame)
    cv2.imshow('Canny kenar algılama', corners)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

"""
NOT :  corners = cv2.Canny(gray, 100, 200) İÇİN

100: Alt Eşik (Low Threshold) değeri.
Bu değer, zayıf kenarları belirler. Gradyan büyüklüğü bu eşik değerinin altında olan pikseller kenar olarak kabul edilmez.
Çok düşük bir değer, gürültüden kaynaklanan istenmeyen kenarların tespit edilmesine neden olabilir.

200: Üst Eşik (High Threshold) değeri.
Bu değer, güçlü kenarları belirler. Gradyan büyüklüğü bu eşik değerinin üzerinde olan pikseller güçlü kenar olarak kabul edilir.
Yüksek eşik değerine sahip kenarlar kesin olarak tespit edilir ve zayıf kenarlar bu güçlü kenarlarla bağlantılıysa kabul edilir.
"""

"""
Gradyan Kavramı
Bir görüntüdeki her piksel, komşu piksellerle karşılaştırıldığında bir yoğunluk farkı gösterir. Gradyan, bu yoğunluk farkının ne 
kadar hızlı ve ne kadar büyük olduğunu ölçer. Daha spesifik olarak:
Gradyan, bir noktadaki yoğunluk değişiminin yönünü ve büyüklüğünü (şiddetini) tanımlar.
Gradyan büyüklüğü ise, bu değişimin ne kadar güçlü olduğunu (yani, değişimin büyüklüğünü) belirler.
"""