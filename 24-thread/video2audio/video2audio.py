from moviepy import editor
import os
import time
from threading import Thread

input_dir = "video"
output_dir = "audio"


os.makedirs(output_dir, exist_ok=True)


def convert(filename, filepath):
    if filepath.endswith(".mp4"):
        output_filepath = os.path.join(output_dir, filename.replace(".mp4", ".mp3"))
        video = editor.VideoFileClip(filepath)
        video.audio.write_audiofile(output_filepath)


def main():
# For 1 thread
    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        convert(filename, filepath)

# Multi threading
start_time = time.perf_counter()

threads = []
for filename in os.listdir(input_dir):
    filepath = os.path.join(input_dir, filename)    
    threads.append(Thread(target=convert, args=[filename, filepath]))

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time.perf_counter()
print(end_time - start_time)


# For 1 thread:

# if __name__ == "__main__":
#     start_time = time.perf_counter()
#     main()
#     end_time = time.perf_counter()
#     total_time = end_time - start_time
#     print(f"Total time : {total_time} seconds")   