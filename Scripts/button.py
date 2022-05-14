import pygame
from pygame.color import THECOLORS
from display import Display
#- self.size[0] / 2
"""Сделать загружку кантинок, исправить местоположение"""
class Button():
    """Button"""
    def __init__(self, text, x, y):
        self.screen = pygame.display.get_surface()
        self.text = text.lower()
        self.size = (150, 40) #(Длина - w, высота - h)
        self.position = [x, y]
        self.image = pygame.Surface(self.size).convert()
        self.image.fill(THECOLORS['red'])
        self.prefire = False

        self.buttons = ["play", "settings", "exit", "back", "fullscreen"]
        

    def draw(self):
        font_ = pygame.font.SysFont('name', 30)
        text = font_.render(self.text, True, THECOLORS['black'])
        self.screen.blit(self.image, (self.position))
        self.screen.blit(text, (self.position[0] + 50, self.position[1] + 10))

    def click(self):
        click = pygame.mouse.get_pressed(5)
        #c_up = pygame.mouse.get_focused() функция проверяющая вышла ли мышь за пределы игры
        #c_up = pygame.mouse.set_pos(0, 0) кидает мышь в указанную точку


        if click[0]:
            mouse_position = pygame.mouse.get_pos()
            x_ = self.position[0] <= mouse_position[0] <= self.position[0] + self.size[0]
            y_ = self.position[1] <= mouse_position[1] <= self.position[1] + self.size[1]
            if x_ and y_ and self.prefire == False: 
                self.image.fill(THECOLORS['blue'])
                if self.text in self.buttons: return self.text
           # elif x_ and y_: self.image.fill(THECOLORS['green'])
            else: self.prefire = True
        else: 
            self.image.fill(THECOLORS['red'])
            self.prefire = False
