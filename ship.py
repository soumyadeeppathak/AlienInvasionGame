import pygame
from pygame import sprite
from pygame.sprite import Sprite

class Ship(Sprite):
    """all the main functioning of the ship is here"""
    def __init__(self, ai_game):
        """initializes the screen and the starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and its rect
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

        #store the horizontal position of the ship in decimal format
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """to respond to the input of the player and move"""
        #update the ship's x value not the rect as the speed depends on it
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update the rect value now as it will be used for diaplsy
        #it will store only integer portion of the ship's x but its ok
        self.rect.x = self.x

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """recenters the ship once aliens hit it"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)