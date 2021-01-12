import pygame

class Rocket:

    def __init__(self, rg_game):
        #the screen properties
        self.screen = rg_game.screen
        self.setting = rg_game.setting
        self.screen_rect = rg_game.screen.get_rect()
        
        #the image properties
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #positional arguments
        self.rect.center = self.screen_rect.center

        #coordinates in decimal format
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_top = False

    def update(self):
        """responding to the input from players"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed

        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed
        if self.moving_top and self.rect.top > 0:
            self.y -= self.setting.ship_speed
        

        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)