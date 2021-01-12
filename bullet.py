import pygame
from pygame import sprite
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class to manage all bullet attributes"""

    def __init__(self, ai_game):
        """create bullet object at ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        #create the bullet rect
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullet in form of decimal
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        #move the bullet according to the decimal value
        self.y -= self.settings.bullet_speed
        #store the integer vale of the y coordinate
        self.rect.y = self.y
    
    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)