import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to create our ship"""
    def __init__(self, ai_settings, screen,):
        """Initialise the ship and its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load image of ship, resize it and get its rect
        big_ship = pygame.image.load('images/ship.bmp')
        small_ship = pygame.transform.scale(big_ship, (75, 75))
        self.image = small_ship
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each ship at the bottom, in the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value for ship's center
        self.center = float(self.rect.centerx)

        # Movement flag:
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position depending on the movements flag's status"""
        # update the ship's center value (not the rect)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx