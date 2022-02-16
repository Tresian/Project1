import pygame
from pygame.color import THECOLORS
from display import Display
#- self.size[0] / 2

class Button():
    def __init__(self, text, x, y):
        self.screen = Display()
        self.text = text.lower()
        self.size = (150, 40) #(Длина, высота)
        self.position = [x, y]
        self.image = pygame.Surface(self.size).convert()
        self.image.fill(THECOLORS['red'])
        

    def draw(self):
        font_ = pygame.font.SysFont('name', 30)
        text = font_.render(self.text, True, THECOLORS['black'])
        self.screen.screen.blit(self.image, (self.position))
        self.screen.screen.blit(text, (self.position[0] + 50, self.position[1] + 10))

    def click(self):
        """При зажатии кнопки мыши косаясь кнопки, она срабатывает, переделать"""
        mouse_position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #c_up = pygame.mouse.get_focused() функция проверяющая вышла ли мышь за пределы игры
        #c_up = pygame.mouse.set_pos(0, 0) кидает мышь в указанную точку

        prefire = False

        x_ = self.position[0] <= mouse_position[0] <= self.position[0] + self.size[0]
        y_ = self.position[1] <= mouse_position[1] <= self.position[1] + self.size[1]


        if x_ and y_ and prefire: pass
        elif x_ and y_ and prefire == False: 
            if click[0] == True:
                self.image.fill(THECOLORS['blue'])
                if self.text == 'play': return self.text
                if self.text == 'exit': return self.text
                if self.text == 'settings': return self.text
            else: self.image.fill(THECOLORS['green'])
        else: self.image.fill(THECOLORS['red'])
