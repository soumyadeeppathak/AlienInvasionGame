import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in a fleet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # load the fleet image
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #defining the position at top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storing the exact position in decimal format
        self.x = float(self.rect.x)