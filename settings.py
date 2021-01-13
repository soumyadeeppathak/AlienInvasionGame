class Setting:
    """class to store all the settings for the game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #ship setting
        self.ship_speed = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3 

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #direction is +1 if right and -1 if left
        self.fleet_direction = 1
