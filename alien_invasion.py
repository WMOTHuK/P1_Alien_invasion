"""Alien invasion main module"""
#Standart imports

import pygame
from pygame.sprite import Group

#Local imports
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats


def run_game():
    """Initializes game and creates a screen"""
    config = Settings()
    pygame.init()
    screen = pygame.display.set_mode(
        (config.screen_width,config.screen_height)
        )
    pygame.display.set_caption("Alien invasion")
    stats = GameStats(config)

    # Ship creation
    ship = Ship(config,screen)

    #Bullet grouping
    bullets = Group()

    #Aliens grouping
    aliens = Group()

    #Alien fleet creation
    gf.create_fleet(config, screen, ship, aliens)

    # Launch main game cycle.
    while True:
        gf.check_events(config,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(config, screen, ship, bullets, aliens)
            gf.update_aliens(config, stats, screen, ship, aliens, bullets)
            gf.update_screen(config, screen, ship, aliens, bullets)

run_game()

