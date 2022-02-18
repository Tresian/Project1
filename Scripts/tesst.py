import pygame, time
from pygame import draw
from pygame.color import THECOLORS
#from display import Display
from button import Button
from enemy import Enemy
from menu import Menu

"""Сделать правильное отслеживание клавиш, доработать стрельбу по клику мыши, сделать правильное движение врагов, Произвести оптимизацию код"""

"""Сделать правильное меню, для загрузки меню используется разные объекты экранов, 
изменения разрешения в одном меню, не сохранятся в другом"""

pygame.init()

#screen = Display()

def main():

    while True:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and keys[pygame.K_ESCAPE]: return



if __name__ == '__main__':
	main()
