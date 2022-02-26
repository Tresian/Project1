from typing import Tuple
import pygame
from pygame.color import THECOLORS
from bullet import Bullet

"""сделать полет пули не по нажатию кнопки"""

class Gun():
    def __init__(self, hero_position: list = None):
        self.screen = pygame.display.get_surface()
        self.position = (hero_position[0], hero_position[1])
        self.size = (5, 5)
        self.pos = None
        self.image = pygame.Surface(self.size).convert()
        self.image.fill(THECOLORS['green'])
        self.rect = pygame.Rect(self.position, self.size)
        self.bullets = []
        self.mouse_position = tuple()

    def control(self, hero_pos: list):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed(5)
        self.draw()
        self.move(hero_pos)
        self.fire(mouse[0])
        self.check_bullets()

    def draw(self): self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, pos: list): 
        if pos[0] and pos[1] is None: pass
        else: self.rect.centerx, self.rect.centery = pos[0], pos[1]

    def fire(self, key = None):
        self.mouse_position = pygame.mouse.get_pos()
        self.pos = self.mouse_position
        if key == True: self.bullets.append(Bullet(self.rect, self.mouse_position))

    def check_bullets(self):
        #изменить удаление пуль
        if self.bullets != []:
            for bullet in self.bullets:
                bullet.position = bullet.control()
                if bullet.rect.centerx == self.mouse_position: self.bullets.pop(0) #0
                if bullet.rect.centerx == self.pos[0] and bullet.rect.centery == self.pos[1]: self.bullets.pop(0)
        else: pass
