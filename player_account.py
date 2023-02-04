import pygame as pg
import sys


def start_game():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()


if __name__ == "__main__":
    start_game()