import random
import arcade


class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = game.width // 2
        self.center_y = 47
        self.width = 67
        self.height =47
        self.speed = 17
    
class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height + 24
        self.angle = 180
        self.speed = 3

class Game(arcade.Window):
    def __init__(self):
        super().__init__( width=720, height=800)
        arcade.set_background_color(arcade.color.PURPLE_HEART)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self)
        self.enemy = Enemy(self)



    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        self.enemy.draw()

    def on_update(self, delta_time: float):
        self.enemy.center_y -= self.enemy.speed


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97: # left a
            self.me.center_x = self.me.center_x - self.me.speed
            ...

        elif symbol == 100: # right d
            self.me.center_x = self.me.center_x + self.me.speed
            


window = Game() 

arcade.run()
 