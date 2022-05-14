import pygame
from menu import Menu

class Game():
	def __init__(self):
		pygame.init()

		self.menu = Menu()

	def run(self): self.menu.run()


if __name__ == '__main__':
	game = Game()
	game.run()