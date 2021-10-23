from Entity.Enemy import Enemy
from Window.Window import Window
import pygame

class Airplane(Enemy):
    def __init__(self, width, height, pos_x, pos_y, image, score):
        super(Enemy, self).__init__(width, height, pos_x, pos_y, image)
        self.image = pygame.transform.rotate(self.image, 180)
        self.health = 50
        self.speed = 2
        self.hit_end = False
        self.hit_start = True
        self.score_award = 100
        self.score = score

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def move(self):

        self.rect.y += (self.get_speed() - 1) 

        if not self.hit_end:
            self.move_right()

            if self.rect.right >= Window.WIDTH:
                self.hit_start = False
                self.hit_end = True

        if not self.hit_start:
            self.move_left()

            if self.rect.left <= 0:
                self.hit_end = False 
                self.hit_start = True 

        
    def update(self):
        self.move()
        
        if self.rect.x >= Window.HEIGHT:
            self.kill()
        
        if self.health == 0:
            self.score.set_score(self.score.get_score() + self.score_award)
            self.kill()
            
