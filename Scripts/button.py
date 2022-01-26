import pygame
from pygame.color import THECOLORS
import room_1

class Button():
    def __init__(self, screen, text, x, y):
        self.screen = screen.screen
        self.text = text.lower()
        self.size = (150, 40) #(Длина, высота)
        self.position = [x - self.size[0] / 2, y]
        self.image = pygame.Surface(self.size).convert()
        self.image.fill(THECOLORS['red'])

    def control(self):
        self.draw()
        self.click()

    def draw(self):
        font_ = pygame.font.SysFont('name', 30)
        text = font_.render(self.text, True, THECOLORS['black'])
        self.screen.blit(self.image, (self.position))
        self.screen.blit(text, (self.position[0] + 50, self.position[1] + 10))

    def click(self):
        mouse_position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        x_ = self.position[0] <= mouse_position[0] <= self.position[0] + self.size[0]
        y_ = self.position[1] <= mouse_position[1] <= self.position[1] + self.size[1]
        
        if x_ and y_:
            if click[0] == True:
                self.image.fill(THECOLORS['blue'])
                if self.text == 'play': return room_1.cycle()
                if self.text == 'exit': 
                    pygame.quit()
                    exit()
                if self.text == 'Settings': return self.text
            else: self.image.fill(THECOLORS['red'])
        else: self.image.fill(THECOLORS['red'])
