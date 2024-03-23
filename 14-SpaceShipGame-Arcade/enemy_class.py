import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height + 24
        self.angle = 180
        self.speed = 3

    def move(self):
        self.center_y -= self.speed
        self.speed += 0.01