""" Ship related classes"""
#Standard imports
import pygame

class Ship():
    def __init__(self, screen):
        """Initializes a ship and sets default position"""
        self.screen = screen

        # Loading ship image
        self.image = pygame.image.load('images/starship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Appears at the bottom of the screen initially
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draws a ship at current position"""
        self.screen.blit(self.image, self.rect)