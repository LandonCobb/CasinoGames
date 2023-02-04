import pygame as pg
import sys
import random

class Bet:
    def __init__(self, amount, number=None, color=None, even=False, odd=False, range=None):
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

wheel = pg.image.load("roulette-assets\paintroulette_smol.png")

list_of_things = [(154, 325), (161, 260), (176, 200), (237, 148), (323, 162), (379, 219), (387, 270), (390, 329), (374, 380), (318, 424), (235, 433), (196, 411), (168, 375)]

numbers = [0, 8, 3, 10, 1, 4, 7, 12, 9, 2, 5, 6, 11]

slots = []

piece_size = 75
betting_board = [[pg.Rect(((piece_size + 5) * col) + 692, ((piece_size + 5) * row) + 28, piece_size, piece_size) for col in range(5)] for row in range(5)]


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
    window.blit(wheel, (20, 20))
    display_board(betting_board)
    
def display_board(betting_board):
    for row in range(len(betting_board)):
        for col in range(len(betting_board[row])):
            pg.draw.rect(window, (0, 0, 0), betting_board[row][col])

def start_game():
    global window
    window = pg.display.set_mode((1200, 680))
    pg.display.set_caption("Roulette")
    spun = False
    chosen = None
    init_slots()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                # code to easily save mouse positions
                # with open("cords.txt", "a") as cords:
                #     cords.write(", ".join(map(str, event.pos)))
                #     cords.write("\n")
                
                spun = True
                chosen = random.randint(0, len(slots) - 1)
                print(slots[chosen].number)
                play_ball_animation(chosen)
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