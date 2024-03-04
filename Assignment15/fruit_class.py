import random
import arcade

class Fruit(arcade.Sprite):
        def __init__(self, game, width = 25, height = 25):
            super().__init__()
            self.width = width
            self.height = height
            self.center_x = random.randint(20, game.width - 20)
            self.center_y = random.randint(20, game.height - 20)
            self.change_x = 0
            self.change_y = 0


class Apple(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.texture = arcade.load_texture("apple.png")

class Pear(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.texture = arcade.load_texture("pear.png")

class Shit(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.texture = arcade.load_texture("shit.png")