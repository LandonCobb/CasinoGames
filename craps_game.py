import pygame as pg
import sys


class Dice:
    def __init__(self, value):
        self.value = value

    def payout(self):
        pass


pg.init()

window = pg.display.set_mode((840, 680))
pg.display.set_caption("Craps")


def start_game():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()


if __name__ == "__main__":
    start_game()
