import pygame, sys
import os
from params import *
from Entity.Fighter import Fighter
from Entity.Enemy import Enemy
from Entity.Airplane import Airplane

pygame.init()

BLACK_COLOR = (0, 0,0)
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

FPS = 60

# IMAGES
F22_IMAGE = os.path.join('media' , 'f22.png')
ENEMY     = os.path.join('media', 'airp.png')  
# FIGHTER GROUP
fighter = Fighter(70, 60, 500, 200, F22_IMAGE, 5)
fighter_group = pygame.sprite.Group()
fighter_group.add(fighter)

# BULLET GROUP
bullet_group = pygame.sprite.Group()

# ENEMY GROUP
enemy_group = pygame.sprite.Group()
enemy_group.add( Airplane(60, 40, 100, 100, ENEMY))
enemy_group.add( Airplane(60, 40, 200, 200, ENEMY))
enemy_group.add( Airplane(60, 40, 300, 300, ENEMY))

#Game loop
def main():
    start_ticks = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    running = True
    while running:
        seconds = (pygame.time.get_ticks() - start_ticks)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_r]:    
            bullet_group.add(fighter.shoot_bullet())
         
        enemy_hits  = pygame.sprite.groupcollide(enemy_group, bullet_group, False, False, pygame.sprite.collide_mask)
        bullet_hits = pygame.sprite.groupcollide(bullet_group, enemy_group, False, False, pygame.sprite.collide_mask)

        for bullet in bullet_hits:
            bullet.kill()

        for enemy in enemy_hits:
            enemy.get_shot()

        
        screen.fill(BLACK_COLOR)
        # SPRITE UPDATE   
        enemy_group.update()
        bullet_group.update()
        fighter_group.update()
        # SCREEN FILL
        # SPRITE DRAW
        enemy_group.draw(screen)
        bullet_group.draw(screen)
        fighter_group.draw(screen)
        # DISPLAY FLIP
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
