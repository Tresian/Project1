import pygame
from pygame.color import THECOLORS

"""сделать уничтожение пуль при достижении поставленной точки, взять основу у движения героя, сделать движение лесенкой а не углами
    Пуля не доходит до точки на 2 пикселя по х и у как и главный герой
"""

class Bullet():
    def __init__(self, gun_position, mouse_position):
        self.screen = pygame.display.get_surface()
        self.mouse_position = mouse_position
        self.position = (gun_position[0], gun_position[1])
        self.size = (5, 5)
        self.speed = 4.0
        self.image = pygame.Surface(self.size)
        self.image.fill(THECOLORS['purple'])
        self.rect = pygame.Rect(self.position, self.size)

    def control(self):
        self.draw()
        self.move()
        return self.rect

    def draw(self): self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        if self.mouse_position[0] > self.rect.centerx and self.mouse_position[1] > self.rect.centery:
            self.rect.centerx += self.speed
            self.rect.centery += self.speed
        if self.mouse_position[0] < self.rect.centerx and self.mouse_position[1] < self.rect.centery:
            self.rect.centerx -= self.speed
            self.rect.centery -= self.speed
        if self.mouse_position[0] > self.rect.centerx and self.mouse_position[1] < self.rect.centery:
            self.rect.centerx += self.speed
            self.rect.centery -= self.speed
        if self.mouse_position[0] < self.rect.centerx and self.mouse_position[1] > self.rect.centery:
            self.rect.centerx -= self.speed
            self.rect.centery += self.speed
