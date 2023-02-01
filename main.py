import pygame
import pygame_menu
import roulette_game

# while True:
#    print('poop')

pygame.init()
menu_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
roulette_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def roulette():
    print(name)
    main_menu.close()
    main_menu.mainloop(roulette_screen)
    pass


def leonardo():
    pass


def craps():
    pass


def playerAccount():
    pass


main_menu = pygame_menu.Menu('Welcome', 1700, 1050, theme=pygame_menu.themes.THEME_BLUE)
roulette_menu = pygame_menu.Menu('Welcome', 1700, 1050, theme=pygame_menu.themes.THEME_BLUE)

name = main_menu.add.text_input('Name :', default="LeBron James").get_value()  # can store this value somewhere
main_menu.add.button('Roulette Table', roulette_game.start_game)
main_menu.add.button('Black Jack', leonardo)
main_menu.add.button('Craps', craps)
main_menu.add.button('See Balance', playerAccount)
main_menu.add.button('Quit', pygame_menu.events.EXIT)

main_menu.mainloop(menu_screen)
