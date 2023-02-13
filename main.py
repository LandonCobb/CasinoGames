import pygame, pyautogui, pygame_menu, sys

from craps_game import CrapsGame
from player_money import PlayerMuns
from roulette_game import Roulette
from slots_game import Slots

pygame.init()
screen_width, screen_height = pyautogui.size()
base_screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.update()

money = 1

def run_roulette():
    roulette = Roulette(money)
    roulette.start_game()

def run_craps():
    craps = CrapsGame(money)
    craps.start_game()

def run_slots():
    slots = Slots(money)
    slots.start_game()

def playerAccount():
    muns = PlayerMuns(money)
    muns.start_menu()

def quit_game():
    with open("money.txt", "w") as file:
        file.write(str(money))
        pygame.quit()
        sys.exit()


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

main_menu.add.button('Roulette Table', run_roulette)
main_menu.add.button('Shits', run_craps)
main_menu.add.button('Slots', run_slots)
main_menu.add.button('See Balance', playerAccount)
main_menu.add.button('Quit', quit_game)

def start_main(user_money = 10000):
    global money
    money = user_money
    main_menu.mainloop(base_screen)
