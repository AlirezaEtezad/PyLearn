import cv2
import numpy as np

my_image = np.ones((500, 800), dtype=np.uint8) * 255

# my_image = np.random.random((250, 350)) * 255
# my_image = np.array(my_image, dtype=np.uint8)

cv2.rectangle(my_image, (30, 35), (350,420), 128, 4)
cv2.circle(my_image, (200, 200), 100, 120, 10)
cv2.line(my_image, (100, 100), (150, 150), 128, 30)
cv2.putText(my_image, "hi im writing...", (200, 200), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, 100)



cv2.imshow("", my_image)
cv2.waitKey()
print(my_image)