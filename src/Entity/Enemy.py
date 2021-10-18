import pygame

from Entity.Entity import Entity
from params import *


class Enemy(Entity):
    def __init__(self, width, height, pos_x, pos_y, image):
        super().__init__(width, height, pos_x, pos_y, image)
        self.speed = 2 
        self.health = 100

    def update(self):
        self.rect.y += 1  
        
        # DESTROYS ITSELF ON IMPACT WITH THE BOTTOM OF THE SCREEN
        if self.rect.bottom >= WIN_HEIGHT:
            self.kill()
        
        if self.health == 0:
            self.kill()

    def get_health(self):
        return self.health()

    def get_shot(self):
        self.health -= 1

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed
