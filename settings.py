import pygame.image


class Settings:
    """A class to store all settings for the game"""

    def __init__(self):
        """Initialise the games static settings"""
        # Screen settings:
        self.screen_width = 1100
        self.screen_height = 750
        self.bg = pygame.transform.scale((pygame.image.load('images/background.bmp')), (1100, 750))
        self.bg_colour = (15, 15, 15)

        # music settings:
        self.laser = pygame.mixer.Sound('sounds/laser.mp3')
        self.explosion = pygame.mixer.Sound('sounds/explosion.mp3')

        # Bullet settings:
        self.bullet_width = 50
        self.bullet_height = 15
        self.bullet_colour = (0, 255, 0)
        self.bullets_allowed = 3

        # ship settings:
        self.ship_limit = 3

        # Alien settings:
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Fleet direction of 1 represents right, -1 will represent left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase settings that change throughout the game and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
