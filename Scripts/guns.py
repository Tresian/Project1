import pygame
from pygame.color import THECOLORS
from bullet import Bullet

"""сделать полет пули не по нажатию кнопки"""

class Gun():
    def __init__(self, screen, hero_position: list = None):
        self.screen = screen
        self.position = (hero_position[0], hero_position[1])
        self.size = (5, 5)
        self.pos = None
        self.image = pygame.Surface(self.size).convert()
        self.image.fill(THECOLORS['green'])
        self.rect = pygame.Rect(self.position, self.size)
        self.bullets = []

    def control(self, x, y):
        keys = pygame.key.get_pressed()
        self.draw()
        self.move(x, y)
        self.check_bullets()

    def draw(self): self.screen.screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, x, y): 
        if x and y is None: pass
        else: self.rect.centerx, self.rect.centery = x, y

    def fire(self, key = None):
        mouse_position = pygame.mouse.get_pos()
        self.pos = mouse_position
        if key == True: self.bullets.append(Bullet(self.screen, self.rect, mouse_position))

    def check_bullets(self):
        #изменить удаление пуль
        if self.bullets != []:
            for bullet in self.bullets:
                bullet.position = bullet.control()
                if bullet.rect.centerx > self.screen.size[0]: self.bullets.pop(0)
                if bullet.rect.centerx == self.pos[0] and bullet.rect.centery == self.pos[1]: self.bullets.pop(0)
        else: pass
