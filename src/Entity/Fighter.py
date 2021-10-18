import pygame
from Entity.Entity import Entity
from Entity.Bullet import Bullet
from params import * 

class Fighter(Entity):
    def __init__(self, width, height, pos_x, pos_y, image, speed):
        super().__init__(width, height, pos_x, pos_y, image)
        self.image = pygame.transform.rotate(self.image, -90)
        self.speed = speed;
    
    def shoot_bullet(self):
        return Bullet(self.rect.center[0], self.rect.center[1])

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def update(self):
        key_pressed = pygame.key.get_pressed()
        
        # MOVEMENT
        if key_pressed[pygame.K_UP]:
            self.move_up()
        
        if key_pressed[pygame.K_DOWN]:
            self.move_down()
        
        if key_pressed[pygame.K_LEFT]:
            self.move_left()
        
        if key_pressed[pygame.K_RIGHT]:
            self.move_right()
        
        # MOVEMENT CONSTAINTS
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT 
        
        if self.rect.left < 0:
            self.rect.left = 0;

        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH

    def move_left(self):
        self.rect.x -= self.get_speed() 

    def move_right(self):
        self.rect.x += self.get_speed() 

    def move_up(self):
        self.rect.y -= self.get_speed()     

    def move_down(self):
        self.rect.y += self.get_speed() 
