import pygame.font


class Button():
    """A class that creates a button to play/start/restart the game."""

    def __init__(self, ai_settings, screen, msg):
        """Initialise button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_colour = (100, 175, 200)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The message only needs to be prepped once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn the message into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_colour, self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then a message"""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
