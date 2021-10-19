import pygame, sys
import os
from Entity.Fighter import Fighter
from Entity.Enemy import Enemy
from Entity.Airplane import Airplane
from Window.Window import Window

pygame.init()

BLACK_COLOR = (0, 0, 0)

#################### WINDOW ###################
window = Window()

#################### FPS ###################
FPS = 60

#################### IMAGES ##################
F22_IMAGE = os.path.join('media', 'f22.png')
ENEMY     = os.path.join('media', 'airp.png')  
BG_IMAGE  = os.path.join('media', 'background.png') 
################### FIGHTER GROUP ##################
fighter = Fighter(50, 40, 500, 200, F22_IMAGE, 5)
fighter_group = pygame.sprite.Group()
fighter_group.add(fighter)
###################
BG = pygame.image.load(BG_IMAGE)
BG = pygame.transform.scale(BG, (Window.WIDTH, Window.HEIGHT))

################### BULLET GROUP ################
bullet_group = pygame.sprite.Group()

################### ENEMY GROUP ####################
enemy_group = pygame.sprite.Group()


################### ENEMY SPAWN EVENT SET #################
spawn_delay = 3000
change_event = pygame.USEREVENT + 1
pygame.time.set_timer(change_event, spawn_delay)


################### EVENTS ######################
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
        if event.type == change_event:
            enemy_group.add( Airplane(80, 60, 100, -100, ENEMY) ) 


################### MAIN LOOP ###################
start_ticks = pygame.time.get_ticks()
clock = pygame.time.Clock()
running = True
x = 0
while running:
    seconds = int((pygame.time.get_ticks() - start_ticks)/1000)
    clock.tick(FPS)
    # EVENTS
    events()

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_r]:    
        bullet_group.add(fighter.shoot_bullet())

    enemy_hits  = pygame.sprite.groupcollide(enemy_group, bullet_group, False, False, pygame.sprite.collide_mask)
    bullet_hits = pygame.sprite.groupcollide(bullet_group, enemy_group, False, False, pygame.sprite.collide_mask)

    for bullet in bullet_hits:
        bullet.kill()

    for enemy in enemy_hits:
        enemy.get_shot()
        
    # SCREEN FILL
    window.get_screen().fill(BLACK_COLOR)
    # BACKGROUND
        
    window.get_screen().blit(BG, (0, x))
    window.get_screen().blit(BG, (0, -Window.HEIGHT + x))
    if x == Window.HEIGHT:
        x = 0
    x += 1
    # SPRITE UPDATE   
    enemy_group.update()
    bullet_group.update()
    fighter_group.update()
    # SPRITE DRAW
    enemy_group.draw(window.get_screen())
    bullet_group.draw(window.get_screen())
    fighter_group.draw(window.get_screen())
    # DISPLAY FLIP
    pygame.display.flip()


