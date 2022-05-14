from calendar import c
from tkinter import CENTER
import pygame, time
from pygame.color import THECOLORS
from display import Display
from button import Button


pygame.init()


screen = Display(False)
s = pygame.display.get_surface()


def main():
    while True:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and keys[pygame.K_f]: pass
            if event.type == pygame.KEYDOWN and keys[pygame.K_v]: pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: exit()
        

        screen.update('white')
        


if __name__ == '__main__':
	main()
