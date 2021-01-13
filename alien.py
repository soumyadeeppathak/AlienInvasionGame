from settings import Setting
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in a fleet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the fleet image
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #defining the position at top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storing the exact position in decimal format
        self.x = float(self.rect.x)

    def update(self):
        """move aliens to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        """return true if it has hit the edges"""
        screen_rect = self.screen.get_rect()

        if(self.rect.right >= screen_rect.right or self.rect.left <= 0):
            return True