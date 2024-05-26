import time
import cv2

image = cv2.imread("media_input/bat.png")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width = image.shape

threshold = 100

start_time = time.time()

for r in range(height):                # 0.09
    for c in range(width):
        if image[r, c] > threshold:
            image[r, c] = 0
        else:
            image[r, c] = 255

# a = image[image > threshold] =  255  # 0.0003
# b = image[image <= threshold] = 0

# _, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY) #2.4!!!
cv2.putText(image, "Bat Man", (height//2, width //2 + width//6), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, 100)

end_time = time.time()

print(end_time - start_time)
cv2.imshow("", image)
cv2.imwrite("media_output/bat.jpg",image)
cv2.waitKey()
