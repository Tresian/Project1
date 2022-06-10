import pygame, time
from pygame.color import THECOLORS
from display import Display
from button import Button
from heroes import Hero


pygame.init()


screen = Display(False)
s = pygame.display.get_surface()



class Hero_1(Hero):
    def __init__(self):
        super().__init__()
        
        self.current_health = 100
        self.max_health = 100
        self.target_health = self.max_health
        self.health_ratio = self.max_health / 300


    def advanced_health(self):
        transition_width = 0
        transition_color = THECOLORS['red']

        if self.current_health < self.target_health: 
            self.current_health += self.health_cheange_speed
            transition_width = int((self.target_health - self.current_health)//self.health_ratio) # Скорость хила
            transition_color = THECOLORS['green']
        elif self.current_health > self.target_health: 
            self.current_health -= self.health_cheange_speed
            transition_width = int((self.target_health - self.current_health)//(-self.health_ratio)) # Скорость урона
            transition_color = THECOLORS['yellow']

        health_bar_rect = pygame.Rect(10, 25, self.current_health // self.health_ratio, 15)
        #print(health_bar_rect.right)
        transition_bar_rect = pygame.Rect(health_bar_rect.right, 25, self.target_health - self.current_health//self.health_ratio, 15)

        pygame.draw.rect(self.screen, transition_color, health_bar_rect)
        pygame.draw.rect(self.screen, transition_color, transition_bar_rect)
        pygame.draw.rect(self.screen, THECOLORS['white'], (10, 25, self.health_bar_lenght, 15), 1)

    def control(self) -> None:
        super().draw()
        self.advanced_health()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]: 
            self.get_damage(20) 
        if keys[pygame.K_e]: 
            self.get_health(20)

hero = Hero_1()

def main():
    while True:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and keys[pygame.K_f]: pass
            if event.type == pygame.KEYDOWN and keys[pygame.K_v]: pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: exit()
        

        screen.update('black')
        hero.control()

        pygame.draw.rect(pygame.display.get_surface(), THECOLORS['white'], (500, 100, 50, 500), 1)
        #                                                                  (x,   y,   len,  height)


if __name__ == '__main__':
	main()
