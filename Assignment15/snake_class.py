
import arcade

from fruit_class import Apple
from fruit_class import Pear
from fruit_class import Shit






class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0
        self.BODY = []

    def set_body_colors(self):
        for i in range(len(self.BODY)):
            if i % 2 == 0:
                self.BODY[i]["color"] = arcade.color.GREEN
            else:
                self.BODY[i]["color"] = arcade.color.GREEN_YELLOW

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, arcade.color.GREEN) # Changed color to GREEN
        for part in self.BODY:
            arcade.draw_rectangle_filled(part["x"], part["y"], self.width, self.height, part["color"])

    def draw_score(self):
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14) 

    def move(self, food):
        self.BODY.append({"x":self.center_x, "y":self.center_y})
        if len(self.BODY) > self.score:
            self.BODY.pop(0)

        if self.center_x < food.center_x:
            self.center_x += self.speed
        elif self.center_x > food.center_x:
            self.center_x -= self.speed
        
        if self.center_y < food.center_y:
            self.center_y += self.speed
        elif self.center_y > food.center_y:
            self.center_y -= self.speed        

    def eat(self, food):
        if isinstance(food, Apple):
            self.score += 1
        elif isinstance(food, Pear):
            self.score += 2
        elif isinstance(food, Shit):
            self.score -= 1
      #  print(self.score)


