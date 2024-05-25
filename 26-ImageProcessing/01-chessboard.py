import cv2
import numpy as np

board_size = 8
square_size = 50

# Create an empty black image
image = np.zeros((board_size * square_size, board_size * square_size), dtype=np.uint8)

# Fill the image with a chessboard pattern
for i in range(board_size):
    for j in range(board_size):
        if (i + j) % 2 == 0:
            color = 255
        else:
            color = 0

        top_left_x = j * square_size
        top_left_y = i * square_size
        
        # Draw the rectangle (square) on the image
        cv2.rectangle(image, (top_left_x, top_left_y), (top_left_x + square_size, top_left_y + square_size), color, -1)

cv2.imshow("Chessboard", image)
cv2.imwrite("images/chessboard.jpg", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
