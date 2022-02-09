import pygame
from pygame import draw
from display import Display
from menu import Menu
from heroes import Hero

"""Сделать правильное отслеживание клавиш, доработать стрельбу по клику мыши, сделать правильное движение врагов, Произвести оптимизацию код"""

"""Сделать правильное меню, для загрузки меню используется разные объекты экранов, 
изменения разрешения в одном меню, не сохранятся в другом"""

"""Меню открывается в файле мейн, по этому работает 2 файла. Выяснить несет ли это сильную нагрузку или же нет. 
Попытаться от этого избавиться"""

pygame.init()

screen = Display()


def menu():
	menu = Menu(screen)
	hero = Hero(screen, color = 'black')
	mouse_x, mouse_y = None, None

	while True:
		for event in pygame.event.get():
			mouse_buttons = pygame.mouse.get_pressed(5) # typle()
			if mouse_buttons[2]:
				try: mouse_x, mouse_y = event.pos[0], event.pos[1]
				except AttributeError: pass

			if event.type == pygame.QUIT:
				pygame.quit()
				exit()


		menu.control()
		hero.control(mouse_x, mouse_y)
		pygame.display.update() # for update obj on screen
		screen.update()


if __name__ == '__main__':
	menu()
