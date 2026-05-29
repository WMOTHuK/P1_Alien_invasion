"""Game statitstics"""

class GameStats():
    """Game stats."""
    def __init__(self, config):
        """Initializes stats"""
        self.config = config
        self.game_active = False
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        """Reset dynamic stats"""
        self.ships_left = self.config.ship_limit
        self.score = 0
        self.level = 1
