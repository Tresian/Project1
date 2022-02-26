import pygame
from pygame.color import THECOLORS


class Display():
    "Создание главного экрана"
    def __init__(self, _FULLSCREEN = True, name_used: str = None):
        pygame.init()
        """pygame.RESIZABLE позволяет изменять размеры окна
        pygame.FULLSCREEN позволяет развернуть окно на весь экран"""
        
        
        if _FULLSCREEN == True:
            self.size = pygame.display.list_modes()[0]
            self.screen = pygame.display.set_mode(self.size)
        else: 
            self.size = [1400, 800]
            self.screen = pygame.display.set_mode(self.size)

        #print(self.size, name_used, hash(id(name_used)))
        
        self.title = pygame.display.set_caption("Project1")
        self.icon = pygame.image.load('Picture/6.jpg')
        pygame.display.set_icon(self.icon)
        
        self.FPS = 60
        self.clock = pygame.time.Clock()


    def update(self, color: str = "black", surf = None):
        if surf: pass
        else:
            self.screen.fill(THECOLORS[color])
            self.clock.tick(self.FPS)

    def new(self, _FULLSCREEN: bool = False) -> bool:
        if _FULLSCREEN:
            self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
            return True
        elif _FULLSCREEN == False: 
            self.screen = pygame.display.set_mode(self.size)
            return False

