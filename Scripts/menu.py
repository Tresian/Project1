import pygame 
from pygame.color import THECOLORS
from button import Button

class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.Surface(self.screen.size)
        self.surf.fill(THECOLORS["white"])
        self.buttons = [Button(screen, "Play", 100, 100), Button(screen, "Setings", 100, 200), Button(screen, "Exit", 100, 300)]

    def control(self):
        self.screen.screen.blit(self.surf, (0, 0))

        for _ in self.buttons:
            _.control()
                