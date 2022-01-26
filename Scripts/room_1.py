import pygame
from display import Display
from heroes import Hero

screen = Display()


def cycle():
    hero = Hero(screen)
    mouse_x, mouse_y = None, None

    while 1:
        for event in pygame.event.get():
            mouse_buttons = pygame.mouse.get_pressed(5) # typle()
            if mouse_buttons[2]:
                try: mouse_x, mouse_y = event.pos[0], event.pos[1]
                except AttributeError: pass

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        print("room_1")
        hero.control(mouse_x, mouse_y)
        pygame.display.update() # for update obj on screen
        screen.update()