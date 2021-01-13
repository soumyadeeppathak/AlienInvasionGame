class GameStats:
    """Track statstics for the game Alien Invasion"""

    def __init__(self, ai_game):
        self.settings= ai_game.settings
        self.reset_stats()
        #check the game active status
        self.game_active = True
    
    def reset_stats(self):
        """initializes statistics that can reset during the games"""
        self.ship_left = self.settings.ship_limit