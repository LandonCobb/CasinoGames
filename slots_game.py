import pygame as pg
import sys
import random

slotValues = [1, 2, 3, 4, 5]

slotResult1 = random.choice(slotValues)
slotResult2 = random.choice(slotValues)
slotResult3 = random.choice(slotValues)
print(slotResult1)
print(slotResult2)
print(slotResult3)

pg.init()

window = None
maxwell = pg.image.load("slots_assets/maxwell.png")

window = pg.display.set_mode((840, 680))


def draw_objects():
    window.fill((255, 255, 255))
    window.blit(maxwell, (20, 20))


def start_game():
    global window
    pg.display.set_caption("Slots")
    window = pg.display.set_mode((1200, 680))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        draw_objects()
        pg.display.update()


if __name__ == "__main__":
    start_game()