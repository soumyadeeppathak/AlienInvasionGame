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
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """to respond to the input of the player and move"""
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)