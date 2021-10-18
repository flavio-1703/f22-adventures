import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((2, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))

    def update(self):
        self.rect.y -= 10
        
        if self.rect.y <= -100:
            self.kill()
