import pygame
from pygame import draw
from pygame.color import THECOLORS
from display import Display
from menu import Menu

"""Сделать правильное отслеживание клавиш, доработать стрельбу по клику мыши, сделать правильное движение врагов, Произвести оптимизацию код"""

"""Сделать правильное меню, для загрузки меню используется разные объекты экранов, 
изменения разрешения в одном меню, не сохранятся в другом"""

pygame.init()

screen = Display()


def menu():
	menu = Menu(screen)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		menu.control()
		pygame.display.update() # for update obj on screen
		screen.update()


def cycle():

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		pygame.display.update() # for update obj on screen
		screen.update()


if __name__ == '__main__':
	menu()
