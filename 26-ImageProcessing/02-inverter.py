import os
import cv2

image_folder = "images"
files = os.listdir(image_folder)
 
for file in files:
    file_path = os.path.join(image_folder, file)
    image = cv2.imread(file_path)

    if image is not None:
        height, width, channels = image.shape
       # print(f"Processing {file}: {height}x{width}x{channels}")

        for i in range(height):
            for j in range(width):
                image[i,j] = 255 - image[i,j]


        inverted_image_path = os.path.join(image_folder, f"inverted_{file}")
        cv2.imwrite(inverted_image_path, image)
    else:
        print(f"Skipping {file}, not a valid image file")


cv2.destroyAllWindows()

