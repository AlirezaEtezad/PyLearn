import cv2

image = cv2.imread("Designer(1).jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)




print(gray_image.shape)
#image = cv2.imread("Designer(1).jpeg")
#cv2.imwrite("gray_image.jpg", gray_image)
#cv2.imshow("alaki", gray_image)



print(gray_image)



print(gray_image[700][750])
gray_image[0:30, 0:1024] = 0


cv2.imshow("alaki", gray_image)





cv2.waitKey()