import pygame

"сделать правильно скиллы, cooldown не должен работать по нажатию кнопки"


class Skill():
    def __init__(self):
        self.element = ['fire', 'water', 'air', 'earth']
        self.cooldown_time = 10.0

    def cooldown(self, cd = None):
        #сделать перезарядку скиллов и спользуя методы pygame
        if cd == True:
            self.cooldown_time -= 0.5
            if self.cooldown_time <= 0:
                return False
            else: return True
        else: return False

class Teleport(Skill):
    def __init__(self):
        self.cooldown_time = 10.0

    def tp(self):
        mouse_position = pygame.mouse.get_pos()
        x, y = mouse_position[0], mouse_position[1]
        self.cooldown(True)
        return x, y

    def use(self):
        return self.tp()
