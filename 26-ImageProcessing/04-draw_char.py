import cv2
import numpy as np

# Define the dimensions of the image
height = 500
width = 500

# Create an empty white image
image = np.ones((height, width), dtype=np.uint8) * 255

# Define the text properties
text = "A"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 10
thickness = 20
color = 0

# Get the size of the text
(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)

# Calculate the center position of the text
x = (width - text_width) // 2
y = (height + text_height) // 2

# Put the text on the image
cv2.putText(image, text, (x, y), font, font_scale, color, thickness)

cv2.imshow("Character A", image)
cv2.imwrite("images/charA.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
