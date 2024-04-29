from threading import Thread
from multiprocessing import Process
from time import time
import requests


def download(url, name):
    result = requests.get(url)


    f = open(name, "wb")
    f.write(result.content)
    f.close()


urls = [["https://offdc.com/wp-content/uploads/2021/04/new-slide-1.jpg", "img1.jpg"],
        ["https://news-cdn.varzesh3.com/pictures/2024/04/28/D/pudslrs5.jpg?w=791", "img2.jpg"],
        ["https://news-cdn.varzesh3.com/pictures/2024/04/28/D/z1zucq4i.jpg?w=791", "img3.jpg"],
        ["https://news-cdn.varzesh3.com/pictures/2024/04/28/D/vh1miiuy.jpg?w=791", "img4.jpg"],
        ["https://news-cdn.varzesh3.com/pictures/2024/04/29/A/anm0bf1g.jpg?w=791", "img5.jpg"],
        ["https://news-cdn.varzesh3.com/pictures/2024/04/18/C/dh0zex4y.jpg", "img5.jpg"],
        ["https://offdc.com/wp-content/uploads/2021/04/new-slide-1.jpg", "img6.jpg"],
        ["https://news-cdn.varzesh3.com/pictures/2024/04/28/D/pudslrs5.jpg?w=791", "img7.jpg"],
        ["https://news-cdn.varzesh3.com/pictures/2024/04/28/D/z1zucq4i.jpg?w=791", "img8.jpg"],
        ["https://news-cdn.varzesh3.com/pictures/2024/04/28/D/vh1miiuy.jpg?w=791", "img9.jpg"],
        ["https://news-cdn.varzesh3.com/pictures/2024/04/29/A/anm0bf1g.jpg?w=791", "img10.jpg"],
        ["https://news-cdn.varzesh3.com/pictures/2024/04/18/C/dh0zex4y.jpg", "img11.jpg"]]



start_time = time()

# for url, name in urls:
#     download(url, name)

threads = []

for url, name in urls:
    threads.append(Thread(target=download, args=[url, name]))
   # threads.append(Process(target=download, args=[url, name]))

for t in threads:
    t.start()

for t in threads:
    t.join()

    


end_time = time()

print(end_time - start_time)