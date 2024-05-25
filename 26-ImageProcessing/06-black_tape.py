import os
import cv2

image_folder = "images"
files = os.listdir(image_folder)
 
for file in files:
    file_path = os.path.join(image_folder, file)
    image = cv2.imread(file_path)

    if image is not None:
        # Get the dimensions of the image
        height, width = image.shape[:2]
        y = 0
        empty_left = width // 6
        thickness = empty_left // 4
        #print(empty_left, thickness)

        for i in range(empty_left):
            image[y ,empty_left: empty_left + thickness ]= 0
            empty_left -= 1
            y += 1

        for i in range(thickness):
            image[y, 0: thickness] = 0
            y += 1
            thickness -= 1

        cv2.imshow("Black Tape", image)
        dead_image_path = os.path.join(image_folder, f"dead_{file}")
        cv2.imwrite(dead_image_path, image)
        cv2.waitKey(0)
