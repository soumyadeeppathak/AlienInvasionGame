class Setting:
    """class to store all the settings for the game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #ship setting
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3 