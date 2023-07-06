import cv2
import numpy as np

# membaca gambar
img = cv2.imread('rachael.jpg')

# mengambil tinggi dan lebar gambar
rows,cols = img.shape[:2]

# membuat matriks translasi
M = np.float32([[1,0,50],[0,1,50]])

# melakukan translasi gambar
translated_img = cv2.warpAffine(img, M, (cols,rows))

# menampilkan gambar asli dan hasil translasi

cv2.imshow('Translated Image',translated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
