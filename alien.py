import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Initialize the alien and set its starting position"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Load the alien image and set its rect attribute 
        self.image_og = pygame.image.load('alien_invasion/images/alien.bmp')
        self.image = pygame.transform.scale(self.image_og, (40, 40))
        self.rect = self.image.get_rect()
        
        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position.
        self.x = float(self.rect.x)
           
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
        