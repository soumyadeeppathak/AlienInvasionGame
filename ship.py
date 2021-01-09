import pygame

class Ship:
    """all the main functioning of the ship is here"""
    def __init__(self, ai_game):
        """initializes the screen and the starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and its rect
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.center

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)