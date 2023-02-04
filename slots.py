import pygame as pg
import sys

def start_game():
    global window
    window = pg.display.set_mode((1200, 680))
    pg.display.set_caption("Slots")
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()