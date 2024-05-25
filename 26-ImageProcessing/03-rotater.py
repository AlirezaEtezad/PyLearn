import cv2

image = cv2.imread("images/3.jpg")
rotated_image = cv2.rotate(image, cv2.ROTATE_180)

cv2.imshow("Rotated Image", rotated_image)

cv2.waitKey(0)
cv2.imwrite("images/rotated.jpg", rotated_image)

cv2.destroyAllWindows()