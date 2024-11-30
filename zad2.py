import cv2
import numpy as np
import matplotlib.pyplot as plt


def grayscale_mean(image):
    return np.mean(image, axis=2).astype(np.uint8)

def grayscale_weighted(image):
    weights = [0.114, 0.587, 0.299]
    return cv2.transform(image, np.array(weights).reshape(1, 3))

image_path1 = 'unnamed.jpg'
image1 = cv2.imread(image_path1)
image_path2 = 'LANDSCAPE_1280.jpg'
image2 = cv2.imread(image_path2)

gray_mean1 = grayscale_mean(image1)
gray_weighted1 = grayscale_weighted(image1)

gray_mean2 = grayscale_mean(image2)
gray_weighted2 = grayscale_weighted(image2)

plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.title("Oryginalny obraz 1")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title("Skala szarości (średnia) 1")
plt.imshow(gray_mean1, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title("Skala szarości (ważona) 1")
plt.imshow(gray_weighted1, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title("Oryginalny obraz 2")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title("Skala szarości (średnia) 2")
plt.imshow(gray_mean2, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.title("Skala szarości (ważona) 2")
plt.imshow(gray_weighted2, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()

cv2.imwrite('gray_mean1.jpg', gray_mean1)
cv2.imwrite('gray_weighted1.jpg', gray_weighted1)
cv2.imwrite('gray_mean2.jpg', gray_mean2)
cv2.imwrite('gray_weighted2.jpg', gray_weighted2)