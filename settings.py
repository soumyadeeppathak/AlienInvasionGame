class Setting:
    """class to store all the settings for the game"""

    def __init__(self):
        """initialize the static settings of the game"""
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #ship setting
        self.ship_limit = 3

        #bullet settings
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3 

        #alien settings
        self.fleet_drop_speed = 10

        #how quickly the game speeds up
        self.speedup_scale = 1.1

        self._initialize_dynamic()
        

    def _initialize_dynamic(self):
        """initialize all the dynamic settings in the game"""
        self.ship_speed = 1.5

        self.bullet_speed = 1.5

        self.alien_speed = 1.0

        #direction is +1 if right and -1 if left
        self.fleet_direction = 1
    
    def increase_speed(self):
        """increase the speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale