""" Ship related classes"""
#Standard imports
import pygame
from pygame.sprite import Sprite


class Ship():
    def __init__(self, config, screen):
        """Initializes a ship and sets default position"""
        self.screen = screen
        self.ai_settings = config

        # Loading ship image
        self.image = pygame.image.load('images/starship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Moving Flags
        self.moving_right = False
        self.moving_left = False

        # Appears at the bottom of the screen initially
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

    def update(self):
        """Updates position of a ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """Draws a ship at current position"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Places a ship at bottom's center"""
        self.center = self.screen_rect.centerx

class Small_ship(Sprite):
    """small ship for ship count"""
    def __init__(self, config, screen):
        """Initializes and small ship and it's position"""
        super(Small_ship, self).__init__()
        self.screen = screen
        self.config = config

        # Loads an alien image
        self.image = pygame.image.load('images/small_ship.bmp')
        self.rect = self.image.get_rect()