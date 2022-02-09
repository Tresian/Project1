import pygame
from pygame.color import THECOLORS

"""сделать следование за персонажем"""
class Enemy():
    def __init__(self, x, y, screen):
        self.screen = screen
        self.position = (x, y)
        self.size = (50, 50)
        self.speed = 1.0
        self.image = pygame.Surface(self.size).convert()
        self.image.fill(THECOLORS["blue"])
        self.rect = pygame.Rect(self.position, self.size)

    def control(self):
        self.draw()
        self.move()

    def draw(self):
        self.screen.screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        if self.rect.x > self.screen.size[0]:
            self.rect.x = -50.0
        self.rect.x += self.speed
