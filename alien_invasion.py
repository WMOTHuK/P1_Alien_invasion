"""Alien invasion main module"""
#Standart imports

import pygame
from pygame.sprite import Group

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

    # Ship creation
    ship = Ship(config,screen)

    #Bullet grouping
    bullets = Group()

    # Launch main game cycle.
    while True:
        gf.check_events(config,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(config, screen, ship, bullets)

run_game()

