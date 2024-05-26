import cv2
import numpy as np
import imageio

image = cv2.imread("media_input/snow.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width = image.shape

# Parameters for snowfall effect
num_snowflakes = 100
num_frames = 5

frames = []

for _ in range(num_frames):
    # Create a copy of the original image
    frame = image.copy()
    
    # Generate random positions for snowflakes
    for _ in range(num_snowflakes):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        
        # Draw the snowflake as a small white circle
        cv2.circle(frame, (x, y), 2, 255, -1)
    
    frames.append(frame)
    
    
    cv2.imshow("Snowfall", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

imageio.mimsave("media_output/snowfall.gif", frames, duration=0.1)
