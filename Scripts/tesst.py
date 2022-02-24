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
pygame.display.init()
info = pygame.display.list_modes()
a = len(info)
print(a)
print(info[a-1])
print(info[2])
size = (1400, 800)
screen = pygame.display.set_mode(size)

skin = pygame.image.load('Picture/6.jpg')

def main():

    while True:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and keys[pygame.K_f]:
                #size = pygame.display.list_modes()[0]
                #print(info)
                #print(pygame.display.toggle_fullscreen())
                screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
                screen.fill(THECOLORS["white"])
            if event.type == pygame.KEYDOWN and keys[pygame.K_v]:
                print(pygame.display.toggle_fullscreen())
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: exit()



if __name__ == '__main__':
	main()
