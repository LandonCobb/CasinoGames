import pygame, pyautogui, pygame_menu, slots_game, blackjack_game
import roulette_game

pygame.init()
screen_width, screen_height = pyautogui.size()
base_screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.update()

def craps():
    pass


def playerAccount():
    pass


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
main_menu.add.button('Roulette Table', roulette_game.Roulette().start_game)
main_menu.add.button('Black Jack', blackjack_game.start_game)
main_menu.add.button('Slots', slots_game.start_game)
main_menu.add.button('Craps', craps)
main_menu.add.button('See Balance', playerAccount)
main_menu.add.button('Quit', pygame_menu.events.EXIT)

def start_main():
    main_menu.mainloop(base_screen)

if __name__ == "__main__":
    start_main()