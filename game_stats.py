"""Game statitstics"""

class GameStats():
    """Game stats."""
    def __init__(self, config):
        """Инициализирует статистику."""
        self.config = config
        self.game_active = True
        self.reset_stats()
    def reset_stats(self):
        self.ships_left = self.config.ship_limit