# import pytube
from pytube import YouTube

class Media:
    def __init__(self, name, director, IMBD_score, url, duration, casts):
        self.name = name
        self.director = director
        self.IMBD_score = IMBD_score
        self.url = url
        self.duration = duration
        self.casts = casts

    def show_info(self):
        print(self.name)
        print(self.director)
        print(self.IMBD_score)
        print(self.duration)
        print(self.casts)

    def download(self):
        print(self.url)
        link = self.url
        stream = YouTube(link).streams.first()
        stream.download(output_path='./',filename=f'{self.name}.mp4')
        print("Video is downloading...")