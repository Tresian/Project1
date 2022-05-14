import pygame
from pygame.color import THECOLORS
from skills import *
from guns import *
# метод image.load создает повернхность
"""сделать стрельбу, камеру которая будет следовать за игроком"""
"""сделать сортировку аргументов, настроить здоровье"""


class Soul():
	"""Душа Игрока"""
	def __init__(self) -> None:
		self.screen = pygame.display.get_surface()
		self.screen_size = [self.screen.get_width(), self.screen.get_height()]
		self.position = [self.screen_size[0] / 2, self.screen_size[1] / 2]
		self.size = (40, 40)
		self.image = pygame.Surface(self.size)
		self.image.fill(THECOLORS['navy'])
		self.rect = pygame.Rect(self.position, self.size)

	def control(self):
		self.draw()

	def draw(self): 
		self.screen.blit(self.image, (self.rect.x, self.rect.y))


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


class Hero(Soul):
	"""Модель героя"""
	def __init__(self, skin: bool = False, color: str = "white") -> None:
		# Get screen and screen size
		self.screen = pygame.display.get_surface()
		self.screen_size = [self.screen.get_width(), self.screen.get_height()]

		self.position = [self.screen_size[0] / 2, self.screen_size[1] / 2]

		self.stats = {'health': 5, 'speed': 2}

		self.size = (50, 50)

		if skin == True:
			"""сделать регулирование изображения"""
			self.image = pygame.image.load('Picture/6.jpg')
		else:
			self.image = pygame.Surface(self.size)
			self.image.fill(THECOLORS[color])

		self.rect = pygame.Rect(self.position, self.size)

		self.mouse_pos = (0, 0)
		if color == 'white': 
			self.have_gun = True
			self.gun = Gun(self.position)
		else: 
			self.have_gun = False
			self.gun = None
		
		# Health
		self.current_health = 1000
		self.target_health = 1000
		self.max_health = 1000
		self.health_bar_lenght = 300
		self.health_ratio = self.max_health / self.health_bar_lenght
		self.health_cheange_speed = 5
		self.regeniration = 0.1

		# Energy
		self.current_energy = 1000
		self.target_energy = 1000
		self.max_energy = 1000
		self.energy_bar_lenght = 300
		self.energy_ratio = self.max_energy / self.energy_bar_lenght
		self.energy_cheange_speed = 5


	def get_damage(self, amount):
		if self.target_health > 0 and self.target_health - amount >= 0: self.target_health -= amount
		else: self.target_health = 0
		if self.target_health <= 0: self.target_health = 0
	def get_health(self, amount):
		if self.target_health < self.max_health and self.target_health + amount <= self.max_health: self.target_health += amount
		else: self.target_health = self.max_health
		if self.target_health >= self.max_health: self.target_health = self.max_health
	def regen(self):
		if self.target_health < self.max_health and self.target_health + self.regeniration <= self.max_health: self.target_health += self.regeniration
		else: self.target_health = self.max_health
	def advanced_health(self):
		"""сделать чтобы желтая полоса от урона не выходила за границу здоровья"""
		transition_width = 0
		transition_color = THECOLORS['red']

		if self.current_health < self.target_health: 
			self.current_health += self.health_cheange_speed
			transition_width = int((self.target_health - self.current_health)/self.health_ratio) # Скорость хила
			transition_color = THECOLORS['green']
		if self.current_health > self.target_health: 
			self.current_health -= self.health_cheange_speed
			transition_width = int((self.target_health - self.current_health)/(-self.health_ratio)) # Скорость урона
			transition_color = THECOLORS['yellow']

		health_bar_rect = pygame.Rect(10,25,int(self.current_health / self.health_ratio), 15)
		transition_bar_rect = pygame.Rect(health_bar_rect.right, 25, transition_width, 15)

		pygame.draw.rect(self.screen, THECOLORS['red'], health_bar_rect) # здоровье
		pygame.draw.rect(self.screen, transition_color, transition_bar_rect) # отступы
		# Рамка
		pygame.draw.rect(self.screen, THECOLORS['white'], (10, 25, self.health_bar_lenght, 15), 1)

	def get_fatigue(self, amount):
		if self.target_energy> 0 and self.target_energy - amount >= 0: self.target_energy -= amount
		else: self.target_energy = 0
		if self.target_energy <= 0: self.target_energy = 0
	def get_energy(self, amount):
		if self.target_energy < self.max_energy and self.target_energy + amount <= self.max_energy: self.target_energy += amount
		else: self.target_energy = self.max_energy
		if self.target_energy >= self.max_energy: self.target_energy = self.max_energy

	def advanced_energy(self):
		"""Добавить свои значения для энергии"""
		transition_width = 0
		transition_color = THECOLORS['blue']

		if self.current_energy < self.target_energy: 
			self.current_energy += self.energy_cheange_speed
			transition_width = int((self.target_energy - self.current_energy)/self.energy_ratio) # Скорость хила
			transition_color = THECOLORS['white']
		if self.current_energy > self.target_energy: 
			self.current_energy -= self.energy_cheange_speed
			transition_width = int((self.target_energy - self.current_energy)/(-self.energy_ratio)) # Скорость урона
			transition_color = THECOLORS['purple']

		energy_bar_rect = pygame.Rect(10,45,int(self.current_energy/ self.energy_ratio), 15)
		transition_bar_rect = pygame.Rect(energy_bar_rect.right, 45, transition_width, 15)

		pygame.draw.rect(self.screen, THECOLORS['blue'], energy_bar_rect) # здоровье
		pygame.draw.rect(self.screen, transition_color, transition_bar_rect) # отступы
		# Рамка
		pygame.draw.rect(self.screen, THECOLORS['white'], (10, 45, self.energy_bar_lenght, 15), 1)

	def control(self):
		self.advanced_health()
		self.regen()
		self.advanced_energy()
		keys = pygame.key.get_pressed()
		mouse_buttons = pygame.mouse.get_pressed(5) #tuple ()
	
		if mouse_buttons[2]: self.mouse_pos = pygame.mouse.get_pos()
		self.draw()
		self.move()

		if self.have_gun:
			self.gun.control([self.rect.centerx, self.rect.centery])

		if keys[pygame.K_r]: 
			self.get_damage(20) 
			self.get_fatigue(20)
		if keys[pygame.K_e]: 
			self.get_health(20)
			self.get_energy(20)
		#if keys[pygame.K_f]: self.tp.use()
	

