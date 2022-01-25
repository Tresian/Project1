import pygame, control, time
from pygame import draw
from pygame.color import THECOLORS
from display import Display
from button import Button
from heroes import Hero, Magic
from enemy import Enemy
from menu import Menu

"""Сделать правильное отслеживание клавиш, доработать стрельбу по клику мыши, сделать правильное движение врагов, Произвести оптимизацию код"""

"""Сделать правильное меню, для загрузки меню используется разные объекты экранов, 
изменения разрешения в одном меню, не сохранятся в другом"""

pygame.init()

screen = Display()


def game_cycle():
	menu = Menu(screen)
	mouse_x, mouse_y = None, None

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

		#hero.control(mouse_x, mouse_y)

		menu.control()
	
		pygame.display.update() # for update obj on screen
		screen.update()


if __name__ == '__main__':
	game_cycle()
