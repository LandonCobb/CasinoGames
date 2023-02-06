import pygame as pg
import sys
import random

# set the game screen  

pg.init()
pg.display.set_caption("Slots")

window = None
ohNo5 = pg.image.load("slots_assets/ohno.png")
maxwell4 = pg.image.load("slots_assets/maxwell.png")
moyai3 = pg.image.load("slots_assets/moyai.png")
braindead2 = pg.image.load("slots_assets/braindead.png")
you1 = pg.image.load("slots_assets/you.png")
machine = pg.image.load("slots_assets/machine.png")

slot_items = [you1, braindead2, moyai3, maxwell4, ohNo5]

lever = pg.Rect(1550, 10, 50, 300) # , , length height


def draw_objects():
    window.fill((151, 42, 39))  # fill with color


def start_game():
    global window
    window = pg.display.set_mode((2000, 1700))
    draw_objects()
    pg.draw.rect(window, (255, 0, 0), lever)
    window.blit(machine, (50,300))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                if lever.collidepoint(pos):
                    game_logic()
        pg.display.update()


def game_logic():
    slot1 = random.choice(slot_items)
    slot2 = random.choice(slot_items)
    slot3 = random.choice(slot_items)

    window.blit(slot1, (10, 10))
    window.blit(slot2, (10, 10))
    window.blit(slot3, (10, 10))
    print(slot1)
    print(slot2)
    print(slot3)

    pg.display.update()


if __name__ == "__main__":
    start_game()
