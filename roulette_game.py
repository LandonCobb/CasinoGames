import pygame as pg
import sys
import random


class Bet:
    def __init__(self, amount, number=None, color=None, even=None, odd=None, range=None):
        self.amount = amount
        self.number = number
        self.color = color
        self.even = even
        self.odd = odd
        self.range = range

    def payout(self):
        pass


class Slot:
    def __init__(self, number, color, cord):
        self.number = number
        self.color = color
        self.cord = cord


pg.init()

window = None

wheel = pg.transform.scale(pg.image.load(
    "roulette-assets\paintroulette.png"), (700, 500))

list_of_things = [(285, 314), (291, 248), (308, 195), (350, 161), (416, 178), (456, 221),
                    (461, 263), (459, 309), (442, 350), (405, 382), (348, 391), (318, 380), (303, 340)]

numbers = [0, 8, 3, 10, 1, 4, 7, 12, 9, 2, 5, 6, 11]

slots = []


def play_ball_animation(selected):
    playing = True
    position = 0
    loop = 0
    while playing:
        pg.time.delay(100)
        draw_objects()
        pg.draw.circle(window, (0, 0, 0), list_of_things[position], 10.0)
        if selected == position and loop == 2:
            playing = False
        elif position == len(list_of_things) - 1:
            position = 0
            loop += 1
        else:
            position += 1
        pg.display.update()

def draw_objects():
    window.fill((255, 255, 255))
    window.blit(wheel, (10, 10))

def start_game():
    global window
    window = pg.display.set_mode((840, 680))
    pg.display.set_caption("Roulette")
    spun = False
    chosen = None
    init_slots()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            # code to easily save mouse positions
            if event.type == pg.MOUSEBUTTONDOWN:
                # with open("cords.txt", "a") as cords:
                #     cords.write(", ".join(map(str, event.pos)))
                #     cords.write("\n")
                
                spun = True
                chosen = random.randint(0, len(slots) - 1)
                play_ball_animation(chosen)
                print(slots[chosen].number)
        draw_objects()
        if spun:
            pg.draw.circle(window, (0, 0, 0), list_of_things[chosen], 10.0)
        pg.display.update()

def init_slots():
    for i, x in enumerate(list_of_things):
        color = None
        if i == 0:
            color = "green"
        elif i % 2 == 1:
            color = "red"
        elif i % 2 == 0:
            color = "black"
        slots.append(Slot(numbers[i], color, x))

if __name__ == "__main__":
    start_game()
