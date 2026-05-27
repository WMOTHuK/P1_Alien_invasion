""" Game functions"""
import sys
import pygame

def check_events():
    """Listening events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(config, ship, screen):
    """Updates a screen"""
    screen.fill(config.bg_color)
    ship.blitme()

    # Display last loaded screen
    pygame.display.flip()