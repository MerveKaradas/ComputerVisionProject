import cv2

# Görüntüyü yükle
image = cv2.imread('geo.png', 0)  # Grayscale olarak yükle
cv2.imshow('Orjinal Resim', image)

# Gürültü azaltma
blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)

# Canny Kenar Algılama
edges = cv2.Canny(blurred_image, 50, 55)

cv2.imshow('Canny Kenar Algilama', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
