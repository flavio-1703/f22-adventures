from Entity.Enemy import Enemy
from params import *
import pygame

class Airplane(Enemy):
    def __init__(self, width, height, pos_x, pos_y, image):
        super().__init__(width, height, pos_x, pos_y, image)
        self.image = pygame.transform.rotate(self.image, 180)
        self.heath = 50
        self.speed = 2
        self.hit_end = False
        self.hit_start = True
        

    def move(self):

        self.rect.y += 1

        if not self.hit_end:
            self.move_right()

            if self.rect.right >= WIN_WIDTH:
                self.hit_start = False
                self.hit_end = True

        if not self.hit_start:
            self.move_left()

            if self.rect.left <= 0:
                self.hit_end = False 
                self.hit_start = True 

        
    def update(self):
        self.move()
        
        if self.rect.x >= WIN_HEIGHT:
            self.kill()
        
        if self.health == 0:
            self.kill()
