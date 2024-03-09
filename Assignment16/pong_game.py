import random
import arcade


class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.YELLOW
        self.radius = 15
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.speed = 5
        self.width = self.radius * 2
        self.heigth = self.radius * 2

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)




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






class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1080, height=720, title="Pong Game")
        arcade.set_background_color(arcade.color.DARK_PASTEL_PURPLE)
        self.player1 = Rocket(40, self.height//2, arcade.color.RED, "Arete")
        self.player2 = Rocket(self.width-40, self.height//2, arcade.color.BLUE, "Computer")
        self.ball = Ball(self)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width // 2, self.height //2, self.width-30, self.height-30, arcade.color.WHITE, border_width=10)
        arcade.draw_line(self.width//2, 30, self.width//2, self.height-30, color=arcade.color.WHITE, line_width=5 )
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()
        self.player1.draw_score(25, 30)
        self.player2.draw_score(self.width-100, 30)



        arcade.finish_render()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.player1.height < y < self.height - self.player1.height:
            self.player1.center_y = y

    def on_update(self, delta_time: float):
        self.ball.move()

        self.player2.move(self.ball)
        
        if self.ball.center_y < 30 or self.ball.center_y > self.height - 30 :
            self.ball.change_y *= -1

        if arcade.check_for_collision(self.player1, self.ball) or arcade.check_for_collision(self.player2, self.ball):
            self.ball.change_x *= -1


        if self.ball.center_x > self.width:
            print("Goal!!!")
            self.player1.score += 1
            self.ball = Ball(self)

        elif self.ball.center_x < 0:
            print("Goal!!!")
            self.player2.score += 1
            self.ball = Ball(self)

game = Game()
arcade.run()

        