import cv2
import numpy as np
import imageio


image = cv2.imread("media_input/TV.png")
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

# height , width = image.shape


x1 = 96
x2 = 550
y1 = 32
y2 = 287

frames = []
for _ in range(3):
    noise = np.random.random((y2 - y1, x2 - x1)) * 255
    noise = np.array(noise, dtype=np.uint8)
    
    image[y1:y2, x1:x2] = noise

    frame = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    frames.append(frame)


    cv2.imshow("", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()


imageio.mimsave ("media_output/noise.gif", frames, duration=0.1)
