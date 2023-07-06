import cv2
import numpy as np

# Read the image
img = cv2.imread('anime.jpg', 0)

# Apply histogram equalization to enhance the contrast
equ = cv2.equalizeHist(img)

# Display the original and enhanced images
cv2.imshow('Original Image', img)
cv2.imshow('Enhanced Image', equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
