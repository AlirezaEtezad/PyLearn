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

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake")
        arcade.set_background_color(arcade.color.KHAKI)
        self.snake = Snake(self)
        self.food = Apple(self)
        self.game_over = False

    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.snake.draw()
        self.snake.draw_score()
        if self.game_over:
            self.draw_game_over()

    def on_update(self, delta_time: float):
        if self.game_over:
            return

        self.snake.move(self.food)
        self.snake.set_body_colors()

        for i in range(len(self.snake.BODY)):
            for j in range(i+1, len(self.snake.BODY)):
                if arcade.check_for_collision_with_list(self.snake.BODY[i], self.snake.BODY[j]):
                    # print("Snake collided with itself")
                    # print("Game Over")
                    self.game_over = True

        if self.snake.center_x >= self.width or self.snake.center_y >= self.height or self.snake.center_x <=0 or self.snake.center_y <= 0:
            self.game_over = True

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food)
            rand_number = random.randint(1, 7)
            if rand_number == 1:
                self.food = Pear(self)
            elif rand_number == 2:
                self.food = Shit(self)
            else:
                self.food = Apple(self)


    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output, self.width / 2 - 180, self.height / 2, arcade.color.RED, 50 )
  

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

if __name__ == "__main__":
    game = Game()
    arcade.run()
