import pygame, sys
from pygame.color import THECOLORS
from button import Button
from display import Display
from heroes import Hero
from lvl_1 import Lvl_1

"""Сделать контроллер который будет отвечать за переходы между комнатами"""

"""Сделать cooldown для кнопок"""
class Menu():
    def __init__(self):
        pygame.init()

        self.screen = Display(False,'Menu')
        self.hero = Hero(color = 'black')

        self.lvl = Lvl_1(self.screen)

        self.buttons = [
            Button("Play", 50, 100), 
            Button("Settings", 50, 200), 
            Button("Saved", 50, 300),
            Button("Exit", 50, 400)
            ]

 
    def run(self, color: str = "white"):
        while True:
            for event in pygame.event.get():
                mouse_buttons = pygame.mouse.get_pressed(5)

                if event.type == pygame.QUIT: return sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pass


            for _ in self.buttons: 
                _.draw()
                if _.click() == 'play': self.lvl.cycle()
                if _.click() == 'settings': self.settings()
                if _.click() == 'exit': return sys.exit()


            self.hero.control()

            pygame.display.update() # for update obj on screen
            self.screen.update(color)


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
    def __init__(self):
        pass

    def run(self):
        pass


"""сделать наследование от главного класса меню."""
class Overlay(Menu):
    def __init__(self):
        super().__init__(self)
