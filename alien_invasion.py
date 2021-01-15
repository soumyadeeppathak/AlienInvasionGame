import sys
import pygame
from time import sleep


from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

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

        self.stats = GameStats(self)#initialize this before anything else

        self.ship = Ship(self)#as it needs the game to be its argument

        self.bullets = pygame.sprite.Group()#creating a group of bullets

        self.aliens = pygame.sprite.Group()#creating a group of aliens
        self._create_fleet()

        #make a play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """the main loop of the game"""
        while True:
           self._check_events()#this always needs to function

           if self.stats.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """check when the mouse hits the play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:#button rect not active when the play is.
            #reset the increased speeds
            self.settings._initialize_dynamic()
            
            self.stats.reset_stats()#to reset when the play is clicked 2nd time and so on
            self.stats.game_active = True

            #to clear any elements on screen left
            self.aliens.empty()
            self.bullets.empty()

            #to refill the screen again
            self._create_fleet()
            self.ship.center_ship()

            #hide the mouse cursor
            pygame.mouse.set_visible(False)


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
    
    def _check_fleet_edges(self):
        """respond to change in direction when edges are touched"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop the fleet and change the direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        #redraw the screen during each loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #making the bullets visible on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #to draw the alien, draw() method need only one argument i.e. screen
        self.aliens.draw(self.screen)

        #draw the game button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

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
        
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        #check if the bullets have hit the alien
        #if yes remove them
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        """keep the bullet argument false if you want the bullet to pass through 
        and hit all the targets behind it too"""

        if not self.aliens:
            #destroy the bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()


    def _update_aliens(self):
        """contains instruction to move the alien"""
        self._check_fleet_edges()
        self.aliens.update()

        #looking for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #check if the alien has hit the bottom
        self._check_alien_bottom()
    
    def _ship_hit(self):
        """respond to ship being hit by alien"""
        if self.stats.ship_left > 0:
            #decrement the number of available ships
            self.stats.ship_left -= 1

            #reset screen and get rid of bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            #create new fleet and recenter the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause the game so the player can see the instance the ship is hit
            sleep(0.5)
        
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_alien_bottom(self):
        """to check if the alien has hit the bottom"""
        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat it the same as if the ship got hit
                self._ship_hit()
                break

if __name__ == '__main__':
    #make game instance and run the game
    ai = Alieninvasion()
    ai.run_game()