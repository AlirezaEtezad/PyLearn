# import MediaClass
from MediaClass import Media

class Series(Media):
    def __init__(self, episodes):
        super.__init__()
        self.episodes = episodes
        