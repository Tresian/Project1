import pygame 
from pygame.color import THECOLORS
from button import Button
from display import Display
from heroes import Hero

"""Переписать main.py и сделать в этом файле меню, настройки и выход, сделать правильную систему выхода из игры"""
class Menu():
    def __init__(self):
        pygame.init()

        self.screen = Display()
        self.hero = Hero(self.screen, color = 'black')

        self.surf = pygame.Surface(self.screen.size)
        self.surf.fill(THECOLORS["white"])

        self.buttons = [
            Button(self.screen, "Play", 100, 100), 
            Button(self.screen, "Setings", 100, 200), 
            Button(self.screen, "Saved", 100, 300),
            Button(self.screen, "Exit", 100, 400)
            ]

        self.mouse_click = [None, None]


    def run(self):
        while True:
            for event in pygame.event.get():
                mouse_buttons = pygame.mouse.get_pressed(5)

                if mouse_buttons[2]:
                    try: self.mouse_click = [event.pos[0], event.pos[1]]
                    except AttributeError: pass

                if event.type == pygame.QUIT: return exit()

            self.screen.screen.blit(self.surf, (0, 0))

            for _ in self.buttons: _.control()

            self.hero.control(self.mouse_click[0], self.mouse_click[1])

            pygame.display.update() # for update obj on screen
            self.screen.update()


    def settings(self):
        pass


    def menu_exit():
        return exit()

"""сделать наследование от главного класса меню."""
class Overlay(Menu):
    def __init__(self):
        super().__init__(self)
        self.buttons = []

    def run(self):
        while True:
            for event in pygame.event.get():
                mouse_buttons = pygame.mouse.get_pressed(5) # tuple[bool, bool, bool]

                if mouse_buttons[2]:
                    try: pass
                    except AttributeError: pass

                if event.type == pygame.QUIT: return exit()

            self.surf.fill(THECOLORS['pyrple'])
            self.screen.screen.blit(self.surf, (0, 0))

            pygame.display.update()
            self.screen.update()