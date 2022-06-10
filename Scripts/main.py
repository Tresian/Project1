import pygame
from menu import Menu

class Game():
	def __init__(self):
		pygame.init()

		self.menu = Menu()

	def run(self) -> None: self.menu.run()


if __name__ == '__main__':
	Game().run()