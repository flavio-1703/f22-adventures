import pygame, sys
## Game and States
from Game.Game import Game
from Game.States.Splash import Splash
from Game.States.Menu import Menu
from Game.States.Gameplay import Gameplay
from Game.States.GameOver import GameOver 
from Window.Window import Window

################### STATES #####################
pygame.init()

window = Window()
screen = window.get_screen()

states = {
    "SPLASH": Splash(),
    "MENU": Menu(),
    "GAMEPLAY": Gameplay(),
    "GAME_OVER": GameOver(),
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()
