import pygame
from display import Display
from heroes import Hero



class Lvl_1():
    def __init__(self):
        self.screen = Display()
        self.hero = Hero(self.screen)

        self.mouse_click = [None, None]

    def cycle(self): 
        while True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                mouse_buttons = pygame.mouse.get_pressed(5) # typle()

                if mouse_buttons[2]:
                    try: self.mouse_click = [event.pos[0], event.pos[1]]
                    except AttributeError: pass

                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_ESCAPE]: return 

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            self.hero.control(self.mouse_click[0], self.mouse_click[1])
            pygame.display.update() # for update obj on screen
            self.screen.update()