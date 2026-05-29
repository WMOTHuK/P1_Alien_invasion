""" SETTINGS for Alien Invasion game"""
class Settings():
    """ stores game settings"""
    def __init__(self):
        """ Initializes static settings"""
        self.screen_width = 700
        self.screen_height = 1200
        self.bg_color = (230,230,230)
        
        #Ship settings
        self.ship_limit  = 3

        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 30
        self.fleet_direction = 1 # 1 - right, -1 - left

        # Game speedup rate and score scale
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes dynamic settings"""
        self.ship_speed_factor = 0.35
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.7
        self.alien_points = 50
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """increases game speed"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)