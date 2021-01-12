import sys
import pygame

from rgsettings import RocketSettings

from rocket import Rocket

class RocketGame:
    """Contains the basic functionality of the rocket"""

    def __init__(self):
        pygame.init()
        self.setting = RocketSettings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Rocket Game")

        self.rocket = Rocket(self)
    
    def game_loop(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            if event.type == pygame.KEYUP:
                self._keyup_events(event)
                

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.rocket.blitme()
        pygame.display.flip()   

    def _keydown_events(self,event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        if event.key == pygame.K_UP:
            self.rocket.moving_top = True 
        if event.key == pygame.K_DOWN:
            self.rocket.moving_bottom = True

    def _keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_top = False 
        if event.key == pygame.K_DOWN:
            self.rocket.moving_bottom = False                   

if __name__ == '__main__':
    """make the rocket game run"""
    rg = RocketGame()
    rg.game_loop()