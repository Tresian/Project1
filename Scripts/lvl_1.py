import pygame
from display import Display
from heroes import Hero
from enemy import Enemy



class Lvl_1():
    def __init__(self, screen):
        self.screen = screen
        self.hero = Hero()
        self.enemy = Enemy(500, 500)


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
            #self.enemy.control()

            self.screen.update()


if __name__ == '__main__':
    level = Lvl_1(Display(False))
    level.cycle()