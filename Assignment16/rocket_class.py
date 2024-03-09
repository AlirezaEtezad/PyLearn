import arcade



class Rocket(arcade.Sprite):
    def __init__(self, x, y, c, n):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = c
        self.name = n
        self.change_x =0
        self.change_y =0
        self.width = 20
        self.height = 80
        self.speed = 4
        self.score = 0

    def move(self, ball):
        if ball.center_x > game.width // 2:
            if self.center_y > ball.center_y:
                self.change_y = -1
                
            if self.center_y < ball.center_y:
                self.change_y = 1            
            self.center_y += self.change_y * self.speed
            

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def draw_score(self, x, y):
        output = f"Score: {self.score}"
        arcade.draw_text(output, x, y, arcade.color.WHITE, 14) 
