import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y] 
