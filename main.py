import pygame
import pygame_menu

# while True:
#    print('poop')

pygame.init()
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def roulette():
    pass


def leonardo():
    pass


def craps():
    pass


def playerAccount():
    pass


menu = pygame_menu.Menu('Welcome', 800, 600, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default="LeBron James")  # can store this value somewhere
menu.add.button('Roulette Table', roulette)
menu.add.button('Black Jack', leonardo)
menu.add.button('Craps', craps)
menu.add.button('See Balance', playerAccount)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
