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

window = pg.display.set_mode((1200, 680))

wheel = pg.image.load("roulette-assets\paintroulette_smol.png")

list_of_things = [(154, 325), (161, 260), (176, 200), (237, 148), (323, 162), (379, 219), (387, 270), (390, 329),
                  (374, 380), (318, 424), (235, 433), (196, 411), (168, 375)]

numbers = [0, 8, 3, 10, 1, 4, 7, 12, 9, 2, 5, 6, 11]

slots = []
selected_slot = -1

piece_size = 75
betting_board = [
    [pg.Rect(((piece_size + 5) * col) + 692, ((piece_size + 5) * row) + 28, piece_size, piece_size) for col in range(4)]
    for row in range(4)]

# globals for betting
bet_font = pg.font.Font(None, 36) 
bet = 0
up_bet_rect = pg.Rect(890, 504, 36, 40)
down_bet_rect = pg.Rect(890, 584, 36, 40)

def init_slots():
    for i, x in enumerate(list_of_things):
        color = None
        if i == 0:
            color = (0, 255, 0)
        elif i % 2 == 1:
            color = (255, 0, 0)
        elif i % 2 == 0:
            color = (0, 0, 0)
        slots.append(Slot(numbers[i], color, x))
    slots.sort(key=lambda slot : slot.number)

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
    # background color
    window.fill((255, 255, 255))

    # betting elements
    bet_text = bet_font.render(f"{bet}", True, (0, 0, 0))
    window.blit(bet_text, (900, 554))

    up_bet_text = bet_font.render("+", True, (0, 0, 0))
    up_bet_text_rect = up_bet_text.get_rect(center = up_bet_rect.center)
    pg.draw.rect(window, (240, 240, 240), up_bet_rect)
    window.blit(up_bet_text, up_bet_text_rect)
    down_bet_text = bet_font.render("-", True, (0, 0, 0))
    down_bet_text_rect = down_bet_text.get_rect(center = down_bet_rect.center)
    pg.draw.rect(window, (240, 240, 240), down_bet_rect)
    window.blit(down_bet_text, down_bet_text_rect)
    #####

    window.blit(wheel, (20, 20))

    # setting up the betting board
    for i in range(13):
        pg.draw.rect(window, slots[i].color, betting_board[i // 4][i % 4])
        number = bet_font.render(f"{i}", True, (255, 255, 255) if i != selected_slot else (0, 0, 255))
        window.blit(number, betting_board[i // 4][i % 4].center)
    pg.draw.rect(window, (0, 0, 0), betting_board[3][1])
    window.blit(bet_font.render("Black", True, (255, 255, 255) if 13 != selected_slot else (0, 0, 255)), betting_board[3][1])
    pg.draw.rect(window, (255, 0, 0), betting_board[3][2])
    window.blit(bet_font.render("Red", True, (255, 255, 255) if 14 != selected_slot else (0, 0, 255)), betting_board[3][2])
    pg.draw.rect(window, (0, 0, 0), betting_board[3][3])
    submit_text = bet_font.render("Submit", True, (255, 255, 255))
    window.blit(submit_text, betting_board[3][3])

def start_game():
    global window
    global bet
    global selected_slot
    
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

                if up_bet_rect.collidepoint(event.pos):
                    bet += 5
                if down_bet_rect.collidepoint(event.pos):
                    if bet >= 5:
                        bet -= 5
                if betting_board[3][3].collidepoint(event.pos):
                    spun = True
                    chosen = random.randint(0, len(slots) - 1)
                    play_ball_animation(chosen)
                for i in range(15):
                    if betting_board[i // 4][i % 4].collidepoint(event.pos):
                        selected_slot = i
                    

        draw_objects()
        if spun:
            pg.draw.circle(window, (0, 0, 0), list_of_things[chosen], 10.0)
        pg.display.update()

if __name__ == "__main__":
    start_game()
