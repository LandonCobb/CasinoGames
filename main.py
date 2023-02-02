import pygame
import pygame_menu, os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h
surface = pygame.display.set_mode((screen_width, screen_height-60))


def roulette():
    pass


def leonardo():
    pass


def craps():
    pass


def playerAccount():
    pass

mytheme = pygame_menu.Theme(background_color=(181, 129, 214, 255),
                title_background_color=(109, 70, 156),
                title_font_shadow=True)

menu = pygame_menu.Menu('Welcome to a casino', screen_width, screen_height-60, theme=mytheme)

menu.add.text_input('Name :', default="LeBron James")
menu.add.button('Roulette Table', roulette)
menu.add.button('Black Jack', leonardo)
menu.add.button('Craps', craps)
menu.add.button('See Balance', playerAccount)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
