""" Bullet related classes and functions"""
#Standard imports
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Describes bullet and it's behaviour"""
    def __init__(self, config, screen, ship):
        """Creates a bullet in current ship position"""
        super().__init__()
        self.screen = screen

        # Create a bullet at 0,0 and redifine position
        self.rect = pygame.Rect(0, 0, config.bullet_width,config.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Use float to store position.
        self.y = float(self.rect.y)
        self.color = config.bullet_color
        self.speed_factor = config.bullet_speed_factor

    def update(self):
        """Moves bullet up the screen"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

def fire_bullet(config, screen, ship, bullets):
        if len(bullets) < config.bullets_allowed:
            new_bullet = Bullet(config, screen, ship)
            bullets.add(new_bullet)