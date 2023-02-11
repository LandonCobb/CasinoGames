import random
import pygame as pg
import sys
import pyautogui
import pygame.font

screen_width, screen_height = pyautogui.size()
pg.init()
pg.display.set_caption("Shits")
baseSize = (550, 600)

# set back button
window = None
backimg = pg.image.load("slots_assets/back.png")
back = pg.Rect(screen_width - 100, 0, 100, 100)

# set die roll
roll_die = pg.image.load("shits_assets/craps_dice.png")
dice = pg.Rect(1200, 1300, 200, 200)  # size pos

green = (0, 99, 0)
black = (0, 0, 0)
font = pygame.font.Font('andy/design.graffiti.ANDYB.ttf', 150)

# user input box
input_rect = pygame.Rect(1200, 900, 200, 32)
color_active = pygame.Color('white')
color_passive = pygame.Color('white')
color = color_passive

global buttonActive
buttonActive = True
window = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)


def draw_objects():
    window.fill((0, 99, 0))
    # window.blit(bgimag, (0, 0))
    window.blit(backimg, (screen_width - 100, 0))
    window.blit(roll_die, (1200, 1300))


def start_game():
    global win
    pg.draw.rect(window, (0, 0, 0), back)
    user_input = ""
    active = False

    draw_objects()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and buttonActive:
                pos = pg.mouse.get_pos()
                if back.collidepoint(pos):
                    pg.quit()
                    sys.exit()
                if event.type == input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        user_input = user_input[-1]
                    else:
                        user_input += event.unicode

                if dice.collidepoint(pos):  # if player clicks on dice
                    print(pos)
                    roll_result = random.randint(2, 12)
                    # display result
                    text = font.render(" " + str(roll_result)+ " ", True, black, green)
                    text_rect = text.get_rect()

                    text_rect.center = (1300, 600)
                    window.blit(text, text_rect)
                    if roll_result == user_input:
                        print("yippie")

        if active:
            color = color_active
        else:
            color = color_passive

        pg.draw.rect(window, color, input_rect)
        text_surface = font.render(user_input, True, black, green)
        window.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)
        pg.display.flip()
        pg.display.update()


if __name__ == "__main__":
    start_game()
