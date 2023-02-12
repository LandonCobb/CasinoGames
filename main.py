import pygame, pyautogui, pygame_menu, slots_game, blackjack_game

import craps_game
from roulette_game import Roulette

pygame.init()
screen_width, screen_height = pyautogui.size()
base_screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.update()

money = 1

def run_roulette():
    roulette = Roulette(money)
    roulette.start_game()

def craps():
    pass


def playerAccount():
    pass

def quit_game():
    with open("money.txt", "w") as file:
        file.write(str(money))
        pygame.events.EXIT


myimage = pygame_menu.baseimage.BaseImage(
    image_path="menu_assets\casino.png"
)
mainTheme = pygame_menu.Theme(
    background_color=myimage,
    title_font_shadow=True,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE,
    widget_font=pygame_menu.font.FONT_HELVETICA,
    widget_font_color=(112, 131, 111),
    widget_font_size=90)

main_menu = pygame_menu.Menu('Welcome to a casino', screen_width, screen_height, theme=mainTheme)

name = main_menu.add.text_input('Name :', default="LeBron James").get_value()  # can store this value somewhere
main_menu.add.button('Roulette Table', run_roulette)
main_menu.add.button('Black Jack', blackjack_game.start_game)
main_menu.add.button('Slots', slots_game.start_game)
main_menu.add.button('Shits', craps_game.start_game)
main_menu.add.button('See Balance', playerAccount)
main_menu.add.button('Quit', quit_game)

def start_main(user_money = 10000):
    global money
    money = user_money
    print(money)
    main_menu.mainloop(base_screen)
