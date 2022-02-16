import pygame 
from pygame.color import THECOLORS
from button import Button
from display import Display
from heroes import Hero
from lvl_1 import Lvl_1

"""Переписать main.py и сделать в этом файле меню, настройки и выход, сделать правильную систему выхода из игры"""
class Menu():
    def __init__(self):
        pygame.init()

        self.screen = Display()
        self.hero = Hero(self.screen, color = 'black')

        self.lvl = Lvl_1()

        self.surf = pygame.Surface(self.screen.size)
        self.surf.fill(THECOLORS["white"])

        self.buttons = [
            Button("Play", 50, 100), 
            Button("Settings", 50, 200), 
            Button("Saved", 50, 300),
            Button("Exit", 50, 400)
            ]

        self.mouse_click = [None, None]


    def run(self):
        self.surf.fill(THECOLORS['white'])
        while True:
            for event in pygame.event.get():
                mouse_buttons = pygame.mouse.get_pressed(5)

                if mouse_buttons[2]:
                    try: self.mouse_click = [event.pos[0], event.pos[1]]
                    except AttributeError: pass

                if event.type == pygame.QUIT: return exit()

            self.screen.screen.blit(self.surf, (0, 0))

            for _ in self.buttons: 
                _.draw()
                if _.click() == 'play': self.lvl.cycle()
                if _.click() == 'settings': return self.settings()
                if _.click() == 'exit': return exit()


            self.hero.control(self.mouse_click[0], self.mouse_click[1])

            pygame.display.update() # for update obj on screen
            self.screen.update()


    def settings(self):
        self.surf.fill(THECOLORS['purple'])
        while True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                mouse_buttons = pygame.mouse.get_pressed(5)

                if mouse_buttons[2]:
                    try: self.mouse_click = [event.pos[0], event.pos[1]]
                    except AttributeError: pass

                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_ESCAPE]: return self.run()

                if event.type == pygame.QUIT: return exit()

            
            self.screen.screen.blit(self.surf, (0, 0))

            self.hero.control(self.mouse_click[0], self.mouse_click[1])

            pygame.display.update() # for update obj on screen
            self.screen.update()



"""сделать наследование от главного класса меню."""
class Overlay(Menu):
    def __init__(self):
        super().__init__(self)
