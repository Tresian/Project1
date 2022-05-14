import pygame
from pygame.color import THECOLORS

"""сделать следование за персонажем"""
class Enemy():
    def __init__(self, x, y) -> None:
        self.screen = pygame.display.get_surface()
        self.screen_size = [self.screen.get_height(), self.screen.get_width()]
        self.position = (x, y)
        self.size = (50, 50)
        self.speed = 7
        self.image = pygame.Surface(self.size).convert()
        self.image.fill(THECOLORS["blue"])
        self.rect = pygame.Rect(self.position, self.size)

    def control(self):
        self.draw()
        self.move()

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        if self.rect.x > self.screen_size[1]:
            self.rect.x = -50
        self.rect.x += self.speed
