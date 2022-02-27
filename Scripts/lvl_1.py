import pygame
from display import Display
from heroes import Hero



class Lvl_1():
    def __init__(self, screen):
        self.screen = screen
        self.hero = Hero()


    def cycle(self): 
        while True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                mouse_buttons = pygame.mouse.get_pressed(5) # typle()

                if event.type == pygame.KEYDOWN and keys[pygame.K_ESCAPE]: return  

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            self.hero.control()

            self.screen.update()