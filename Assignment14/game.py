import random
import arcade 
from spaceship_class import Spaceship
from enemy_class import Enemy    


    



        
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=720, height=800)
        arcade.set_background_color(arcade.color.PURPLE_HEART)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self)
        # self.enemy = Enemy(self)
        self.ENEMIES = []
        self.first_enemy = Enemy(self)
        self.ENEMIES.append(self.first_enemy)
        self.score = 0
        self.spawn_timer = 0
        self.game_over = False
        self.explosion_sound = arcade.load_sound("mixkit-bomb-explosion-in-battle-2800.wav")
        self.game_over_sound = arcade.load_sound("mixkit-bomb-explosion-in-battle-2800.wav")

    def draw_score(self):
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output, self.width / 2 - 180, self.height / 2, arcade.color.RED, 50 )
        arcade.play_sound(self.game_over_sound)       

    def draw_hearts(self):
        heart_icon = arcade.load_texture("heart.png")
        heart_scale = 0.05  # Adjust this value to scale the size of the hearts
        scaled_width = heart_icon.width * heart_scale
        scaled_height = heart_icon.height * heart_scale
        x = self.width - scaled_width * self.me.lives - 10  # Starting x position for the first heart
        y = scaled_height
        spacing = scaled_width
        for heart in range(self.me.lives):  # Assuming self.me.lives contains the remaining lives
            arcade.draw_texture_rectangle(x, y, scaled_width, scaled_height, heart_icon, 0)
            x += spacing


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        for enemy in self.ENEMIES:
            enemy.draw()

        for bullet in self.me.BULLETS:
            bullet.draw()

        self.draw_score()
        self.draw_hearts()
        if self.game_over:
            self.draw_game_over()

        
         
        

    def on_update(self, delta_time: float):

        if self.game_over:
            return

        self.me.move(self) # Pass the game object as a parameter to the move method
        for enemy in self.ENEMIES:
            if arcade.check_for_collision(enemy, self.me):
                print("You collided an enemy")
                print("Game Over")
                self.game_over = True


                
    #    print(f"Delta Time: {delta_time}, Timer: {self.spawn_timer}")
        
        for enemy in self.ENEMIES:
            enemy.move()

        self.spawn_timer += delta_time
    #    if random.randint(1, 200) == 1: 
        if self.spawn_timer >= 3:   
            self.new_enemy = Enemy(self)
            self.ENEMIES.append(self.new_enemy)
            self.spawn_timer = 0
        

        for bullet in self.me.BULLETS: 
            bullet.move()

        for enemy in self.ENEMIES:
            for bullet in self.me.BULLETS:
                if arcade.check_for_collision(enemy, bullet):
                    self.ENEMIES.remove(enemy)
                    self.me.BULLETS.remove(bullet)
                    self.score = self.score + 1
                    arcade.play_sound(self.explosion_sound)

        for enemy in self.ENEMIES:
            if enemy.center_y < 0:
                self.ENEMIES.remove(enemy)
                self.me.lives -= 1
                      
                if self.me.lives <= 0:
                    self.game_over = True


        for bullet in self.me.BULLETS:
            if bullet.center_y > self.height:
                self.me.BULLETS.remove(bullet)
                                

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A: #97
           # self.me.move("L")
            self.me.change_x = -1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D: #100
           # self.me.move("R")
            self.me.change_x = 1

        elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.me.change_x = 0

        elif symbol == arcade.key.SPACE:
            self.me.fire()
            


window = Game() 
arcade.run()
 