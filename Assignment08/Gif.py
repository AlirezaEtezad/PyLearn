import os
import imageio
# You should just add your pictures in 'gif' folder
file_list =sorted(os.listdir("gif"))

IMAGES = []
for file_name in file_list:
    file_path ="gif/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

# print(IMAGES)
imageio.mimsave("gif/Gif.gif", IMAGES)

