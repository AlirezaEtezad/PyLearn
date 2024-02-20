# import MediaClass
from MediaClass import Media

class Film(Media):
    def __init__(self, genre):
        super.__init__()
        self.genre = genre
    