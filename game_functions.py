""" Game functions"""
#Standard import
import sys
import pygame
#local imports
from bullet import fire_bullet


def check_keydown_events(event, config, screen, ship, bullets):
    """Reacts on push key event"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create new bullet and add it tp group
        fire_bullet(config, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Reacts on release key event"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(config, screen, ship, bullets):
    """Checks key and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, config, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
        bullets.update()
        # Delete bullets, that are out of screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

def update_screen(config, screen, ship, bullets):
    """Updates a screen"""
    screen.fill(config.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Display last loaded screen
    pygame.display.flip()
