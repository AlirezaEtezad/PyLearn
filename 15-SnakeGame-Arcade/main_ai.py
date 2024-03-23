from snake_class import Snake

class Ai:
    def ai_move(self , food):
        if self.center_x < food.center_x:
            self.center_x += self.speed
        elif self.center_x > food.center_x:
            self.center_x -= self.speed
        
        if self.center_y < food.center_y:
            self.center_y += self.speed
        elif self.center_y > food.center_y:
            self.center_y -= self.speed    