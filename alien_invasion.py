"""Alien invasion main module"""
#Standart imports

import pygame

#Local imports
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Initializes game and creates a screen"""
    config = Settings()
    pygame.init()
    screen = pygame.display.set_mode(
        (config.screen_width,config.screen_height)
        )
    pygame.display.set_caption("Alien invasion")
    ship = Ship(config,screen)

    # Launch main game cycle.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(config, ship, screen)
run_game()

