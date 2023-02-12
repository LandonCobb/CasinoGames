import pygame as pg
import pyautogui
import start_main

class PlayerMuns:
    def __init__(self, starting_amount):
        pg.init()
        pg.display.set_caption("Money")
        self.starting_amount = starting_amount
        self.backimg = pg.image.load("slots_assets/back.png")
        self.screen_width, self.screen_height = pyautogui.size()
        self.back = pg.Rect(self.screen_width-100, 0, 100, 100)
        self.image_back = pg.transform.scale(pg.image.load("menu_assets/casino.png"), (self.screen_width, self.screen_height))
        self.give = pg.Rect(900, 800, 800, 100)
        self.get = pg.Rect(900, 500, 800, 100)
        self.window = pg.display.set_mode((self.screen_width, self.screen_height), pg.FULLSCREEN)

    def draw_objects(self):
        self.window.blit(self.image_back, (0, 0))
        self.window.blit(self.backimg, (self.screen_width-100, 0))
        total_text = pg.font.Font(None, 200)
        button_text = pg.font.Font(None, 100)
        self.window.blit(total_text.render(f"${self.starting_amount}", True, (0, 0, 0)), ((self.screen_width/2)-250, 200))
        self.window.blit(button_text.render(f"Deposit $100", True, (0, 0, 0)), (1050, 500))
        self.window.blit(button_text.render(f"Withdraw up to $100", True, (0, 0, 0)), (930,800))

    def start_menu(self):
        while True:
            self.draw_objects()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    if self.back.collidepoint(pos):
                        start_main.start(self.starting_amount)
                    if self.give.collidepoint(pos):
                        self.starting_amount -= 100
                        if self.starting_amount < 0:
                            self.starting_amount = 0
                    if self.get.collidepoint(pos):
                        self.starting_amount += 100
            pg.display.update()

if __name__ == "__main__":
    PlayerMuns().start_game()
