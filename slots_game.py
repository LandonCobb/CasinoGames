import pygame as pg
import sys
import random
import pyautogui

# set the game screen  

screen_width, screen_height = pyautogui.size()
pg.init()
pg.display.set_caption("Slots")
baseSize = (550,600)

window = None
ohNo5 = pg.transform.scale(pg.image.load("slots_assets/ohno.png"), baseSize)
maxwell4 = pg.transform.scale(pg.image.load("slots_assets/maxwell.png"), baseSize)
moyai3 = pg.transform.scale(pg.image.load("slots_assets/moyai.png"), baseSize)
braindead2 = pg.transform.scale(pg.image.load("slots_assets/braindead.png"), baseSize)
you1 = pg.transform.scale(pg.image.load("slots_assets/you.png"), baseSize)
machine = pg.transform.scale(pg.image.load("slots_assets/machine.png"), (screen_width,screen_height))

slot_items = [you1, braindead2, moyai3, maxwell4, ohNo5]

lever = pg.Rect(1550, 10, 50, 300) # , , length height
window = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)


def draw_objects():
    window.fill((151, 42, 39))  # fill with color    
    window.blit(machine, (0,0))  # fill with color

def start_game():
    draw_objects()
    pg.draw.rect(window, (255, 0, 0), lever)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                if lever.collidepoint(pos):
                    draw_objects()
                    game_logic()
        pg.display.update()


def game_logic():
    slot1 = random.choice(slot_items)
    slot2 = random.choice(slot_items)
    slot3 = random.choice(slot_items)

    window.blit(slot1, (393, 500))
    window.blit(slot2, (985, 500))
    window.blit(slot3, (1605, 500))
    print(slot1)
    print(slot2)
    print(slot3)


if __name__ == "__main__":
    start_game()
