import pygame 
from pygame.color import THECOLORS

class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.Surface(self.screen.size)
        self.surf.fill(THECOLORS["white"])

    def draw(self):
        self.screen.screen.blit(self.surf, (self.screen.size[0], self.screen.size[1]))

        
