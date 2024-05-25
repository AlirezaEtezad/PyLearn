import cv2
import numpy as np

height = 765
width = 765

image = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        image[i, j] = int((i / height) * 255)
        #image[i, j] = int(((i + j) / (height + width)) * 255)

cv2.imshow("Gradient", image)
cv2.imwrite("images/gradient.jpg", image)

cv2.waitKey(0)

cv2.destroyAllWindows()