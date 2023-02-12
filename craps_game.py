import pygame.font
import random
import pygame as pg
import sys
import pyautogui
import pygame.font

import start_main


class CrapsGame:
    def __init__(self, starting_amount):
        pg.init()
        self.starting_amount = starting_amount
        self.screen_width, self.screen_height = pyautogui.size()
        pg.display.set_caption("Shits")
        self.green = (0, 99, 0)
        self.black = (0, 0, 0)
        self.font = pygame.font.Font('andy/design.graffiti.ANDYB.ttf', 150)

        # back return button
        self.back_img = pg.image.load("slots_assets/back.png")
        self.back_rect = pg.Rect(self.screen_width - 100, 0, 100, 100)

        # die roll button
        self.roll_die_img = pg.image.load("shits_assets/craps_dice.png")
        self.dice_rect = pg.Rect(1200, 1300, 200, 200)

        # text input
        self.input_rect = pg.Rect(1200, 900, 200, 32)
        self.color_active = pg.Color('red')
        self.color_passive = pg.Color('white')
        self.color = self.color_passive

        # bet input
        self.up_bet_rect = pg.Rect(1100, 1350, 36, 40)
        self.down_bet_rect = pg.Rect(1100, 1400, 36, 40)
        self.bet_amount = 0

        self.window = pg.display.set_mode((self.screen_width, self.screen_height), pg.FULLSCREEN)

    def draw_objects(self):
        self.window.fill(self.green)
        self.window.blit(self.back_img, (self.screen_width - 100, 0))
        self.window.blit(self.roll_die_img, (1200, 1300))

        # show money
        total_text = self.font
        self.window.blit(total_text.render(f"{self.starting_amount}", True, (0, 0, 0)), (10, 26))

        bet_text = self.font.render(f"{self.bet_amount}", True, self.black)
        self.window.blit(bet_text, (950, 1315))

        up_bet_text = self.font.render("+", True, self.black)
        up_bet_text_rect = up_bet_text.get_rect(center=self.up_bet_rect.center)
        self.window.blit(up_bet_text, up_bet_text_rect)

        down_bet_text = self.font.render("-", True, self.black)
        down_bet_text_rect = down_bet_text.get_rect(center=self.down_bet_rect.center)
        self.window.blit(down_bet_text, down_bet_text_rect)

    def display_message(self, message):
        message_text = self.font.render(message, True, (0, 0, 0))
        self.window.blit(message_text, (1000, 100))

    def start_game(self):
        global win
        # pg.draw.rect(self.window, (0, 0, 0), self.back_img)
        user_input = ""
        current_message = ""
        active = False
        self.draw_objects()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.draw_objects()
                    pos = pg.mouse.get_pos()
                    # for back button
                    if self.back_rect.collidepoint(event.pos):
                        start_main.start(self.starting_amount)
                    # for placing a bet
                    if self.up_bet_rect.collidepoint(event.pos):
                        print("up")
                        self.bet_amount += 5
                    if self.down_bet_rect.collidepoint(event.pos):
                        if self.bet_amount >= 5:
                            self.bet_amount -= 5
                    # for dice roll
                    if self.dice_rect.collidepoint(pos):
                        roll_result = random.randint(2, 12)
                        print(f"Result : {roll_result}")
                        print(f"user put : {user_input}")
                        # display result
                        text = self.font.render(f"{roll_result}", True, self.black, self.green)
                        text_rect = text.get_rect()
                        text_rect.center = (1300, 600)
                        self.window.blit(text, text_rect)
                        # check bet (win condition)
                        if str(roll_result) == user_input:
                            if roll_result == 12 or roll_result == 2:
                                self.starting_amount += self.bet_amount * 4
                                current_message = f"OH SHITS, You won {self.bet_amount*4}!"
                            if roll_result == 7:
                                self.starting_amount += self.bet_amount
                                current_message = f"Well duh it was gonna roll 7: {self.bet_amount}!"
                            if 5 >= roll_result <= 10:
                                self.starting_amount += self.bet_amount * 3
                                current_message = f"Nice you win {self.bet_amount * 3}!"
                            if 3 >= roll_result < 11:
                                self.starting_amount += self.bet_amount * 2
                                current_message = f"You won {self.bet_amount * 2}!"
                        else:
                            self.starting_amount -= self.bet_amount
                            current_message = f"You suck-{self.bet_amount}!"
                    # for user input
                    if self.input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode
            if active:
                color = self.color_active
            else:
                color = self.color_passive

            self.display_message(current_message)
            pg.draw.rect(self.window, color, self.input_rect)
            text_surface = self.font.render(user_input, True, self.black, self.green)
            self.window.blit(text_surface, (self.input_rect.x, self.input_rect.y))
            self.input_rect.w = max(100, text_surface.get_width() + 10)
            pg.display.flip()
            pg.display.update()


if __name__ == "__main__":
    CrapsGame().start_game()
