import pygame, control, time
from pygame.color import THECOLORS
from display import Display
from button import Button
from heroes import Hero, Magic
from enemy import Enemy

"""Сделать правильное отслеживание клавиш, доработать стрельбу по клику мыши, сделать правильное движение врагов, Произвести оптимизацию код"""

pygame.init()

"""print(f'button1: {mouse_buttons[0]}, button2: {mouse_buttons[1]}, button3: {mouse_buttons[2]},
button4: {mouse_buttons[3]}, button5: {mouse_buttons[4]}')"""

def menu():
	"""сделать текст на кнопках"""
	screen = Display()
	buttons = [Button(screen, 'Exit', 700, 500), Button(screen, 'Play', 700, 300), Button(screen, 'Settings', 700 , 400)]

	while True:
		for event in pygame.event.get():
			if buttons[0].click() == 'exit': exit()
			if buttons[1].click() == 'play': game_cycle()
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		for button in buttons:
			button.control()
		pygame.display.update() # for update obj on screen
		screen.update()


def game_cycle():
	screen = Display()
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
	menu()
