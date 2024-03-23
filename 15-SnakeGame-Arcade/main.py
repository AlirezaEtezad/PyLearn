import random
import arcade

from snake_class import Snake
from fruit_class import Apple
from fruit_class import Pear
from fruit_class import Shit


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
        if self.snake.score < 0:
            self.game_over = True

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