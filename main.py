import pygame, os, pygame_menu, roulette_game
import blackjack_game
import craps_game
import slots_game

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h
menu_screen = pygame.display.set_mode((screen_width, screen_height-60))
roulette_screen = pygame.display.set_mode((screen_width, screen_height-60))


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

mainTheme = pygame_menu.Theme(background_color=(181, 129, 214, 255),
                title_background_color=(109, 70, 156),
                title_font_shadow=True)

main_menu = pygame_menu.Menu('Welcome to a casino', screen_width, screen_height-60, theme=mainTheme)
roulette_menu = pygame_menu.Menu('Welcome', screen_width, screen_height-60, theme=pygame_menu.themes.THEME_BLUE)


name = main_menu.add.text_input('Name :', default="LeBron James").get_value()  # can store this value somewhere
main_menu.add.button('Roulette Table', roulette_game.start_game)
main_menu.add.button('Black Jack', blackjack_game.start_game)
main_menu.add.button('Craps', slots_game.start_game)
main_menu.add.button('See Balance', playerAccount)
main_menu.add.button('Quit', pygame_menu.events.EXIT)

main_menu.mainloop(menu_screen)
