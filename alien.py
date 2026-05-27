"""Alien related classes and functions"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Describes an alien ship"""
    def __init__(self, config, screen):
        """Initializes and alien and it's position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.config = config

        # Loads an alien image
        self.image = pygame.image.load('images/UFO.bmp')
        self.rect = self.image.get_rect()

        # All new aliens appear in left top corner
        self.rect.x = int(self.rect.width / 2)
        self.rect.y = int(self.rect.height / 2)

        # Saving exact alien position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Returns true if alien reaches the border"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """Draws an alien in current position"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Moves an alien to the right"""
        self.x += (self.config.alien_speed_factor
                   * self.config.fleet_direction)
        self.rect.x = self.x

