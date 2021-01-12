import sys

import pygame

from settings import Setting

from ship import Ship

from bullet import Bullet

from alien import Alien

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

        self.bullets = pygame.sprite.Group()#creating a group of bullets

        self.aliens = pygame.sprite.Group()#creating a group of aliens
        self._create_fleet()

    def run_game(self):
        """the main loop of the game"""
        while True:
           self._check_events()
           self.ship.update()
           self._update_bullet()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()#calling fire the bullet function
    
    def _keyup_events(self, event):
        """respond to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create a new bullet and add it to the groups of the existing bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  

    def _create_fleet(self):
        """create new fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size#so that we do not have to use the rect again and again

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)
        #to make the rows
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        #create first row of alien
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.y = alien_height + 2 * alien_height * row_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_screen(self):
        #redraw the screen during each loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #making the bullets visible on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #to draw the alien, draw() method need only one argument i.e. screen
        self.aliens.draw(self.screen)
        #make most recently drawn screen visible
        pygame.display.flip()
    
    def _update_bullet(self):
        """contains all bullet update code"""
        self.bullets.update()
        
        #getting rid of the bullet after they have disappeared
        for bullet in self.bullets.copy():
            """we use a copy as we can not delete items from a running loop"""
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    #make game instance and run the game
    ai = Alieninvasion()
    ai.run_game()