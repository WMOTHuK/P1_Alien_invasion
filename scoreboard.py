""" Score related classes and functions"""

#Standart imports
import pygame
from pygame.sprite import Group
from ship import Small_ship

class Scoreboard():
    """Game scores output class"""
    def __init__(self, config, screen, stats):
        """Sets scoring atribbutes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.config = config
        self.stats = stats

        # Scoring font setup
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships(stats, config, screen)

    def prep_score(self):
        """Turns text to graphics"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{: }".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.
        text_color, self.config.bg_color)

        # Outputs score top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,
        True,
        self.text_color, self.config.bg_color)
        # Align highscore to the center
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        current_level = str(self.stats.level)
        self.level_image = self.font.render(current_level, True, 
                                            self.text_color,
                                            self.config.bg_color)
        # Outputs level top left
        self.level_rect = self.score_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.top = 20
    
    def prep_ships(self, stats, config, screen, ):
        self.small_ships = Group()
        for i in range(stats.ships_left):
            small_ship = Small_ship(config, screen)
            small_ship.rect.right = ( self.screen_rect.right -
                                     ( small_ship.rect.width * i + 20 ))
            small_ship.rect.top = 70
            self.small_ships.add(small_ship)



    def show_score(self):
        """Outputs score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        for ship in self.small_ships:
            self.screen.blit(ship.image, ship.rect)