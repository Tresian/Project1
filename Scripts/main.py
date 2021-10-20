import pygame, control, time
from pygame.color import THECOLORS
from display import Display
from button import Button
from heroes import Hero, Magic
from enemy import Enemy

"""Сделать правильное отслеживание клавиш, доработать стрельбу по клику мыши, сделать правильное движение врагов, Произвести оптимизацию код"""

"""Сделать правильное меню, для загрузки меню используется разные объекты экранов, 
изменения разрешения в одном меню, не сохранятся в другом"""

pygame.init()

rooms = []

def main_menu():
	"""сделать текст на кнопках"""
	screen = Display()
	buttons = [Button(screen, 'Exit', 700, 500), Button(screen, 'Play', 700, 300), Button(screen, 'Settings', 700 , 400)]

	while True:
		for event in pygame.event.get():
			if buttons[0].click() == 'exit': exit()
			if buttons[1].click() == 'play': 
				print(screen)
				screen.size = [1080, 720] 
				game_cycle()
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		for button in buttons:
			button.control()
		pygame.display.update() # for update obj on screen
		screen.update()

def menu():
	screen = Display()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		pygame.display.update()
		screen.update()

def game_cycle():
	screen = Display()
	print(screen)
	print(screen.info())
	hero = Hero(screen) # переработать
	enemys = []

	mouse_x, mouse_y = None, None
	pressed = False

	while True:
		for event in pygame.event.get():
			mouse_buttons = pygame.mouse.get_pressed(5) # typle()
			if mouse_buttons[2]:
				# исправить ошибку атрибута, возможно исправлена
				try: mouse_x, mouse_y = event.pos[0], event.pos[1]
				except AttributeError: pass
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		"""for enemy in enemys:
			enemy.control()"""
		hero.control(mouse_x, mouse_y)

		pygame.display.update() # for update obj on screen
		screen.update()


if __name__ == '__main__':
	main_menu()
