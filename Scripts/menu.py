import pygame, sys
from pygame.color import THECOLORS
from button import Button
from display import Display
from heroes import Hero
from lvl_1 import Lvl_1

"""Сделать контроллер который будет отвечать за переходы между комнатами"""

"""Сделать cooldown для кнопок"""
class Menu():
    """Главное меню"""
    def __init__(self):
        self.click = True

        self.screen = Display(False)
        self.color = 'white'
        self.hero = Hero(color = 'black')

        self.lvl = Lvl_1(self.screen)
        self.settings = Settings(self.screen)

        self.buttons = [
            Button("Play", 50, 100), 
            Button("Settings", 50, 200), 
            Button("Saved", 50, 300),
            Button("Exit", 50, 400)
            ]
        
 
    def run(self, buttons: list = None) -> None:
        while True:
            for event in pygame.event.get():
                mouse_buttons = pygame.mouse.get_pressed(5)

                if event.type == pygame.QUIT: return sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and buttons != []: return

            if buttons == None:
                for _ in self.buttons: 
                    _.draw()
                    if _.click() == 'play': self.lvl.cycle()
                    if _.click() == 'settings': self.settings.run(self.settings.buttons)
                    if _.click() == 'exit': return sys.exit()
            else:
                for _ in buttons:
                    _.draw()
                    if _.click() == 'fullscreen' and self.click == False: 
                        self.click = self.screen.new(True)
                        pygame.time.delay(700)
                    elif _.click() == 'fullscreen' and self.click:
                        self.click = self.screen.new(False)
                        pygame.time.delay(700)
                    if _.click() == 'back': return


            self.hero.control()

            self.screen.update(self.color)


    def settings(self):
        buttons = [
            Button("Fullscreen", 50, 100),
            Button("Back", 50, 300)
        ]
        a = False
        while True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                mouse_buttons = pygame.mouse.get_pressed(5)

                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_ESCAPE]: return self.run()

                if event.type == pygame.QUIT: return exit()


            for _ in buttons:
                _.draw()
                if _.click() == "fullscreen" and a == False: 
                    a = self.screen.new(True)
                    pygame.time.delay(700)
                elif _.click() == "fullscreen" and a: 
                    a = self.screen.new(False)
                    pygame.time.delay(700)
                if _.click() == "back": return

            self.hero.control()

            pygame.display.update() # for update obj on screen
            self.screen.update("purple")


class Settings(Menu):
    def __init__(self, screen):
        self.screen = screen
        self.click = False
        self.buttons = [
            Button("Fullscreen", 50, 100),
            Button("Back", 50, 300)
        ]

        self.color = 'purple'

        self.hero = Hero(color = 'black')


"""сделать наследование от главного класса меню."""
class Overlay(Menu):
    def __init__(self):
        super().__init__(self)
