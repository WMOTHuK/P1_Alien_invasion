""" Game functions"""
#Standard import
import sys
import pygame
#local imports
from bullet import fire_bullet
from alien import Alien


def check_keydown_events(event, config, screen, ship, bullets):
    """Reacts on push key event"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create new bullet and add it tp group
        fire_bullet(config, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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

def update_bullets(config, screen, ship, bullets, aliens):
        bullets.update()
        # Delete bullets, that are out of screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        check_bullet_alien_collisions(config, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(config, screen, ship, aliens, bullets):
        # Check bullet and aliens collisions
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if len(aliens) == 0:
            bullets.empty()
            create_fleet(config, screen, ship, aliens)

def create_fleet(config, screen, ship, aliens):
    """Creates alien fleet"""
    alien = Alien(config, screen)
    aliennum = get_number_aliens_x(config, screen)
    alien_rows = get_alien_rows(config, alien.rect.height, ship.rect.height)
    # Creating first alien row
    for row_number in range(alien_rows):
        for alien_number in range(aliennum):
            create_alien(config, screen, alien_number, aliens, row_number)

def get_number_aliens_x(config, screen):
    """Calculates alien number in a row"""
    alien = Alien(config, screen)
    alien_width = alien.rect.width
    available_space_x = config.screen_width -  alien_width
    return int(available_space_x / (1.5 * alien_width))

def get_alien_rows(config, alien_height, ship_height):
    """Calculates alien number in a row"""
    available_space_y = (config.screen_height 
                        - alien_height / 2
                        - ship_height * 3)
    return int(available_space_y / (1.5 * alien_height))


def create_alien(config, screen, alien_number, aliens, row_number):
        """Create an alien and position it"""
        alien = Alien(config, screen)
        alien.x = alien.rect.width + 1.5 * alien.rect.width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = (alien.rect.height / 2
                        + alien.rect.height * row_number * 1.5)
        aliens.add(alien)

def update_screen(config, screen, ship, aliens, bullets ):
    """Updates a screen"""
    screen.fill(config.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
     # Display last loaded screen
    pygame.display.flip()


def check_fleet_edges(config,aliens):
    """Checks if fleet reaches borders"""
    for alien in aliens.sprites():
        if alien.check_edges():
           change_fleet_direction(config, aliens)
           break

def change_fleet_direction(config,aliens):
    """changes direction of the fleet"""
    for alien in aliens.sprites():
        alien.rect.y += config.fleet_drop_speed
    config.fleet_direction *= -1

def update_aliens(config, aliens):
    """Refreshes position of all aliens"""
    check_fleet_edges(config, aliens)
    aliens.update()
