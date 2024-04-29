import arcade
from bullet_class import Bullet


class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = game.width // 2
        self.center_y = 47
        self.change_x = 0
        self.change_y = 0
        self.width = 67
        self.height =47
        self.speed = 3
        self.BULLETS = []
        self.lives = 3
        self.laser_sound = arcade.load_sound(":resources:sounds/laser1.wav")


    def move(self, game):

        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x = self.center_x - self.speed


        elif self.change_x == 1:
            if self.center_x < game.width:
                self.center_x = self.center_x + self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.BULLETS.append(new_bullet)
        arcade.play_sound(self.laser_sound)