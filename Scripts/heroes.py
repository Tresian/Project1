from ast import Tuple
import pygame
from pygame.color import THECOLORS
from skills import *
from guns import *
# метод image.load создает повернхность
"""сделать стрельбу, камеру которая будет следовать за игроком"""


class Hero():
	"""Модель героя"""
	def __init__(self, skin: bool = False, color: str = "white"):
		# Get screen and screen size
		self.screen = pygame.display.get_surface()
		self.screen_size = [self.screen.get_width(), self.screen.get_height()]

		self.position = [self.screen_size[0] / 2, self.screen_size[1] / 2]

		self.stats = {'health': 5, 'speed': 2}

		self.size = (50, 50)
		self.surf = pygame.Surface(self.size) 

		if skin == True:
			"""сделать регулирование изображения"""
			self.image = pygame.image.load('Picture/6.jpg')
		else:
			self.image = pygame.Surface(self.size)
			self.image.fill(THECOLORS[color])

		self.rect = pygame.Rect(self.position, self.size)

		self.mouse_pos = (0, 0)
		

	def control(self):
		keys = pygame.key.get_pressed()
		mouse_buttons = pygame.mouse.get_pressed(5) #tuple ()
	
		if mouse_buttons[2]: self.mouse_pos = pygame.mouse.get_pos()
		self.draw()
		self.move()


		#if keys[pygame.K_f]: self.tp.use()

	def draw(self): self.screen.blit(self.image, (self.rect.x, self.rect.y))

	def move(self):
		"""Cлишком быстрое замедление, переписать управление, иногда застревает и не перестает двигаться"""
		"""Переписать передвижение"""
		if self.mouse_pos[0] and self.mouse_pos[1] != self.rect.x and self.rect.y:
			if self.mouse_pos[0] > self.rect.centerx:
				if self.mouse_pos[0] - self.rect.centerx < self.stats['speed'] * 25.0: self.rect.centerx += 1.0
				else: self.rect.centerx += self.stats['speed']
			elif self.mouse_pos[0] < self.rect.centerx:
				if self.rect.centerx - self.mouse_pos[0] < self.stats['speed'] * 25.0: self.rect.centerx -= 1.0
				else: self.rect.centerx -= self.stats['speed']

			if self.mouse_pos[1] > self.rect.centery:
				if self.mouse_pos[1] - self.rect.centery < self.stats['speed'] * 25.0: self.rect.centery += 1.0
				else: self.rect.centery += self.stats['speed']
			elif self.mouse_pos[1] < self.rect.centery:
				if self.rect.centery - self.mouse_pos[1] < self.stats['speed'] * 25.0: self.rect.centery -= 1.0
				else: self.rect.centery -= self.stats['speed']


class Magic(Hero):
	def __init__(self, screen):
		super().__init__(screen)
		self.image.fill(THECOLORS['red'])
