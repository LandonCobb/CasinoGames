import pygame, pyautogui, pygame_menu, roulette_game

pygame.init()
screen_width,screen_height = pyautogui.size()
base_screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.update()

def roulette():
    print(name)
    main_menu.close()
    main_menu.mainloop(base_screen)
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

main_menu = pygame_menu.Menu('Welcome to a casino', screen_width, screen_height, theme=mainTheme)

name = main_menu.add.text_input('Name :', default="LeBron James").get_value()  # can store this value somewhere
main_menu.add.button('Roulette Table', roulette_game.start_game)
main_menu.add.button('Black Jack', leonardo)
main_menu.add.button('Craps', craps)
main_menu.add.button('See Balance', playerAccount)
main_menu.add.button('Quit', pygame_menu.events.EXIT)

main_menu.mainloop(base_screen)