import pygame
from pygame.color import THECOLORS
"реализовать главный экран"

class Display():
    "Создание главного экрана"
    def __init__(self, _FULLSCREEN = False):
        """pygame.RESIZABLE позволяет изменять размеры окна
        pygame.FULLSCREEN позволяет развернуть окно на весь экран"""

        if _FULLSCREEN == True:
            self.size = [1440, 900]
            self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        else: 
            self.size = [1400, 800]
            self.screen = pygame.display.set_mode(self.size)

        self.title = pygame.display.set_caption("Project1")
        self.icon = pygame.image.load('Picture/6.jpg')
        pygame.display.set_icon(self.icon)
        
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def update(self, bg_color = 'black'):
        self.screen.fill(THECOLORS[bg_color])
        self.clock.tick(self.FPS)
