import pygame as pg
import sys


class Dice:
    def __init__(self, value):
        self.value = value

    def payout(self):
        pass

pg.init()

window = None
maxwell = pg.image.load("casino-assets/maxwell.png")

window = pg.display.set_mode((840, 680))


def draw_objects():
    window.fill((255, 255, 255))
    window.blit(maxwell, (20, 20))


def start_game():
    global window
    pg.display.set_caption("Craps")
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