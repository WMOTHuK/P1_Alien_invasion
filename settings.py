""" SETTINGS for Alien Invasion game"""
class Settings():
    """ stores game settings"""
    def __init__(self):
        """ Initializes default settings"""
        self.screen_width = 700
        self.screen_height = 1200
        self.bg_color = (230,230,230)
        
        #Ship settings
        self.ship_speed_factor = 0.25
        self.ship_limit  = 3

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 20
        self.fleet_direction = 1 # 1 - right, -1 - left

        