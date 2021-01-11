import sys

import pygame

from settings import Setting

from ship import Ship

class Alieninvasion:
    """class to manage the working of the game"""

    def __init__(self):
        """initializzes the game and create game resources"""
        pygame.init()
        self.settings = Setting()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)#as it needs the game to be its argument

    def run_game(self):
        """the main loop of the game"""
        while True:
           self._check_events()
           self.ship.update()
           self._update_screen() 
            
            
    def _check_events(self):
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        """respond to key press"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _keyup_events(self, event):
        """respond to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
                
    def _update_screen(self):
        #redraw the screen during each loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #make game instance and run the game
    ai = Alieninvasion()
    ai.run_game()