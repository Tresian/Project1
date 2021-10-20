import pygame
from pygame.color import THECOLORS
from skills import *
from guns import *
# метод image.load создает повернхность
"""сделать стрельбу, камеру которая будет следовать за игроком"""
class Hero():
	"""Модель героя"""
	def __init__(self, screen):
		self.screen = screen
		self.position = [screen.size[0] / 2, screen.size[1] / 2]
		self.size = (50, 50)
		self.speed = 2.0
		self.image = pygame.Surface(self.size).convert() #pygame.image.load("|")
		self.image.fill(THECOLORS["white"])
		self.rect = pygame.Rect(self.position, self.size)
		self.skill = Teleport()
		self.gun = Gun(self.screen, self.position)

	def control(self, x, y):
		keys = pygame.key.get_pressed()
		mouse_buttons = pygame.mouse.get_pressed(5)
		self.draw()
		self.move(x, y)
		if self.gun:
			self.gun.control(self.rect.centerx, self.rect.centery)
			if mouse_buttons[0]: self.gun.fire(True)


	def draw(self): self.screen.screen.blit(self.image, (self.rect.x, self.rect.y))

	def move(self, x, y):
		"""Cлишком быстрое замедление, переписать управление"""
		if x and y != self.rect.centerx and self.rect.y:
			if x > self.rect.centerx:
				if x - self.rect.centerx < self.speed * 25.0: self.rect.centerx += 1.0
				else: self.rect.centerx += self.speed
			elif x < self.rect.centerx:
				if self.rect.centerx - x < self.speed * 25.0: self.rect.centerx -= 1.0
				else: self.rect.centerx -= self.speed
			if y > self.rect.centery:
				if y - self.rect.centery < self.speed * 25.0: self.rect.centery += 1.0
				else: self.rect.centery += self.speed
			elif y < self.rect.centery:
				if self.rect.centery - y < self.speed * 25.0: self.rect.centery -= 1.0
				else: self.rect.centery -= self.speed


class Magic(Hero):
	def __init__(self, screen):
		super().__init__(screen, air)
		self.image.fill(THECOLORS['red'])