import pygame as pg
import sys
import random


class Bet:
    def __init__(self, amount, number=None, color=None):
        self.amount = amount
        self.number = number
        self.color = color
        self.payout_amount = amount
    
    def check_for_win(self, slot):
        if self.number != None:
            if self.number == slot.number:
                self.payout_amount = self.amount * 13
                return True
        elif self.color != None:
            if self.color == slot.color:
                self.payout_amount = self.amount * 2
                return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Bet({self.amount}, {self.number}, {self.color})"

class Slot:
    def __init__(self, number, color, cord):
        self.number = number
        self.color = color
        self.cord = cord

    def __repr__(self):
        return f"Slot({self.number}, {self.color}, {self.cord})"

class Roulette:
    def __init__(self, starting_amount = 1000):
        pg.init()
        
        self.starting_amount = starting_amount

        self.window = pg.display.set_mode((1200, 680))

        self.wheel = pg.image.load("roulette-assets\paintroulette_smol.png")

        # slot globals
        self.slots_cords = [(154, 325), (161, 260), (176, 200), (237, 148), (323, 162), (379, 219), (387, 270), (390, 329),
                        (374, 380), (318, 424), (235, 433), (196, 411), (168, 375)]
        self.numbers = [0, 8, 3, 10, 1, 4, 7, 12, 9, 2, 5, 6, 11]
        self.slots = []
        self.sorted_slots = []
        self.selected_slot = -1

        # creating the betting board
        piece_size = 75
        self.betting_board = [
            [pg.Rect(((piece_size + 5) * col) + 692, ((piece_size + 5) * row) + 28, piece_size, piece_size) for col in range(4)]
            for row in range(4)]

        # globals for betting
        self.bet_font = pg.font.Font(None, 36) 
        self.bet_amount = 0
        self.up_bet_rect = pg.Rect(890, 504, 36, 40)
        self.down_bet_rect = pg.Rect(890, 584, 36, 40)

    def init_slots(self):
        # creates a list of slots in the order they appear clockwise around the board starting at 0
        for i, x in enumerate(self.slots_cords):
            color = None
            if self.numbers[i] == 0:
                color = (0, 255, 0)
            elif self.numbers[i] % 2 == 0:
                color = (0, 0, 0)
            else:
                color = (255, 0, 0)
            self.slots.append(Slot(self.numbers[i], color, x))
        # creates a sorted list based the slot number
        self.sorted_slots = self.slots.copy()
        self.sorted_slots.sort(key=lambda slot : slot.number)

    def play_ball_animation(self, selected):
        playing = True
        position = 0
        loop = 0
        while playing:
            pg.time.delay(100)
            self.draw_objects()
            pg.draw.circle(self.window, (0, 0, 0), self.slots_cords[position], 10.0)
            if selected == position and loop == 2:
                playing = False
            elif position == len(self.slots_cords) - 1:
                position = 0
                loop += 1
            else:
                position += 1
            pg.display.update()
            
    def display_message(self, message):
        message_text = self.bet_font.render(message, True, (0, 0, 0))
        self.window.blit(message_text, (660, 430))

    def draw_objects(self):
        # background color
        self.window.fill((255, 255, 255))

        # amount of money the use has
        total_text = pg.font.Font(None, 20)
        self.window.blit(total_text.render(f"${self.starting_amount}", True, (0, 0, 0)), (1038, 26))

        # betting elements
        bet_text = self.bet_font.render(f"{self.bet_amount}", True, (0, 0, 0))
        self.window.blit(bet_text, (900, 554))

        up_bet_text = self.bet_font.render("+", True, (0, 0, 0))
        up_bet_text_rect = up_bet_text.get_rect(center = self.up_bet_rect.center)
        pg.draw.rect(self.window, (240, 240, 240), self.up_bet_rect)
        self.window.blit(up_bet_text, up_bet_text_rect)
        down_bet_text = self.bet_font.render("-", True, (0, 0, 0))
        down_bet_text_rect = down_bet_text.get_rect(center = self.down_bet_rect.center)
        pg.draw.rect(self.window, (240, 240, 240), self.down_bet_rect)
        self.window.blit(down_bet_text, down_bet_text_rect)
        #####

        self.window.blit(self.wheel, (20, 20))

        # setting up the betting board
        for i in range(13):
            pg.draw.rect(self.window, self.sorted_slots[i].color, self.betting_board[i // 4][i % 4])
            number = self.bet_font.render(f"{i}", True, (255, 255, 255) if i != self.selected_slot else (0, 0, 255))
            self.window.blit(number, self.betting_board[i // 4][i % 4].center)
        pg.draw.rect(self.window, (0, 0, 0), self.betting_board[3][1])
        self.window.blit(self.bet_font.render("Black", True, (255, 255, 255) if 13 != self.selected_slot else (0, 0, 255)), self.betting_board[3][1])
        pg.draw.rect(self.window, (255, 0, 0), self.betting_board[3][2])
        self.window.blit(self.bet_font.render("Red", True, (255, 255, 255) if 14 != self.selected_slot else (0, 0, 255)), self.betting_board[3][2])
        pg.draw.rect(self.window, (0, 0, 0), self.betting_board[3][3])
        submit_text = self.bet_font.render("Submit", True, (255, 255, 255))
        self.window.blit(submit_text, self.betting_board[3][3])

    def start_game(self):
        self.window = pg.display.set_mode((1200, 680))
        pg.display.set_caption("Roulette")
        spun = False
        chosen = None
        bet = None
        current_message = ""
        cheat = False
        self.init_slots()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_CAPSLOCK:
                        cheat = not cheat   

                if event.type == pg.MOUSEBUTTONDOWN:
                    # code to easily save mouse positions #
                    # with open("cords.txt", "a") as cords:
                    #     cords.write(", ".join(map(str, event.pos)))
                    #     cords.write("\n")

                    # checks if the betting board has been clicked on and selects it
                    for i in range(15):
                        if self.betting_board[i // 4][i % 4].collidepoint(event.pos):
                            self.selected_slot = i

                    # betting buttons
                    if self.up_bet_rect.collidepoint(event.pos):
                        self.bet_amount += 5
                    if self.down_bet_rect.collidepoint(event.pos):
                        if self.bet_amount >= 5:
                            self.bet_amount -= 5

                    # checks the submit button
                    if self.betting_board[3][3].collidepoint(event.pos) and self.selected_slot != -1 and self.bet_amount != 0:
                        bet = ""
                        spun = True
                        if cheat:
                            chosen = 0
                        else:
                            chosen = random.randint(0, len(self.slots) - 1)
                        
                        if self.selected_slot == 13:
                            color_chosen = (0, 0, 0)
                        elif self.selected_slot == 14:
                            color_chosen = (255, 0, 0)
                        else:
                            color_chosen = None
                        bet = Bet(self.bet_amount, self.selected_slot if 0 <= self.selected_slot <= 12 else None, color_chosen)
                        print(self.slots[chosen], bet)
                        
                        self.play_ball_animation(chosen)
                        
                        if bet.check_for_win(self.slots[chosen]):
                            current_message = f"You won {bet.payout_amount}!"
                            self.starting_amount += bet.payout_amount
                        else:
                            current_message = f"You lost {bet.amount} :("
                            self.starting_amount -= bet.payout_amount
                        
            self.draw_objects()
            self.display_message(current_message)
            if spun:
                pg.draw.circle(self.window, (0, 0, 0), self.slots_cords[chosen], 10.0)

            pg.display.update()

if __name__ == "__main__":
    Roulette().start_game()