import pygame as pg
import sys
import random


class Bet:
    def __init__(self, amount, number=None, color=None):
        self.amount = amount
        self.number = number
        self.color = color
        self.payout_amount = self.payout()

    def payout(self):
        return 0
    
    def check_for_win(self, slot):
        if self.number != None:
            if self.number == slot.number:
                return True
        elif self.color != None:
            if self.color == slot.color:
                return True
        else:
            return False

class Slot:
    def __init__(self, number, color, cord):
        self.number = number
        self.color = color
        self.cord = cord

    def __repr__(self):
        return f"Slot({self.number}, {self.color}, {self.cord})"


pg.init()

window = pg.display.set_mode((1200, 680))

wheel = pg.image.load("roulette-assets\paintroulette_smol.png")

slots_cords = [(154, 325), (161, 260), (176, 200), (237, 148), (323, 162), (379, 219), (387, 270), (390, 329),
                  (374, 380), (318, 424), (235, 433), (196, 411), (168, 375)]
numbers = [0, 8, 3, 10, 1, 4, 7, 12, 9, 2, 5, 6, 11]

slots = []
sorted_slots = []
selected_slot = -1

piece_size = 75
betting_board = [
    [pg.Rect(((piece_size + 5) * col) + 692, ((piece_size + 5) * row) + 28, piece_size, piece_size) for col in range(4)]
    for row in range(4)]

# globals for betting
bet_font = pg.font.Font(None, 36) 
bet_amount = 0
up_bet_rect = pg.Rect(890, 504, 36, 40)
down_bet_rect = pg.Rect(890, 584, 36, 40)

def init_slots():
    global sorted_slots
    for i, x in enumerate(slots_cords):
        color = None
        if numbers[i] == 0:
            color = (0, 255, 0)
        elif numbers[i] % 2 == 0:
            color = (0, 0, 0)
        else:
            color = (255, 0, 0)
        slots.append(Slot(numbers[i], color, x))
    # sorted_slots = slots
    sorted_slots = slots.copy()
    sorted_slots.sort(key=lambda slot : slot.number)

def play_ball_animation(selected):
    playing = True
    position = 0
    loop = 0
    while playing:
        pg.time.delay(100)
        draw_objects()
        pg.draw.circle(window, (0, 0, 0), slots_cords[position], 10.0)
        if selected == position and loop == 2:
            playing = False
        elif position == len(slots_cords) - 1:
            position = 0
            loop += 1
        else:
            position += 1
        pg.display.update()


def draw_objects():
    # background color
    window.fill((255, 255, 255))

    # betting elements
    bet_text = bet_font.render(f"{bet_amount}", True, (0, 0, 0))
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
        pg.draw.rect(window, sorted_slots[i].color, betting_board[i // 4][i % 4])
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
    global bet_amount
    global selected_slot
    
    window = pg.display.set_mode((1200, 680))
    pg.display.set_caption("Roulette")
    spun = False
    chosen = None
    bet = None
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
                    bet_amount += 5
                if down_bet_rect.collidepoint(event.pos):
                    if bet_amount >= 5:
                        bet_amount -= 5
                if betting_board[3][3].collidepoint(event.pos) and selected_slot != -1 and bet_amount != 0:
                    spun = True
                    chosen = random.randint(0, len(slots) - 1)
                    print(chosen, slots[chosen])
                    
                    if selected_slot == 13:
                        color_chosen = (0, 0, 0)
                    elif selected_slot == 14:
                        color_chosen = (255, 0, 0)
                    else:
                        color_chosen = None
                    bet = Bet(bet_amount, selected_slot if 0 <= selected_slot <= 12 else None, color_chosen)
                    
                    play_ball_animation(chosen)
                    
                    if bet.check_for_win(slots[chosen]):
                        bet_amount = f"You Won {bet_amount}"
                    

                for i in range(15):
                    if betting_board[i // 4][i % 4].collidepoint(event.pos):
                        selected_slot = i
                    

        draw_objects()
        if spun:
            pg.draw.circle(window, (0, 0, 0), slots_cords[chosen], 10.0)
        pg.display.update()

if __name__ == "__main__":
    start_game()
