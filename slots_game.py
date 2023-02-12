import pygame as pg
import sys
import random
import pyautogui
import time
import start_main

class Slots:
    def __init__(self, starting_amount):
        pg.init()
        pg.display.set_caption("Slots")
        self.starting_amount = starting_amount
        self.screen_width, self.screen_height = pyautogui.size()
        self.baseSize = (550,600)
        self.window = pg.display.set_mode((self.screen_width, self.screen_height), pg.FULLSCREEN)
        self.backimg = pg.image.load("slots_assets/back.png")
        self.ohNo5 = pg.transform.scale(pg.image.load("slots_assets/ohno.png"), self.baseSize)
        self.maxwell4 = pg.transform.scale(pg.image.load("slots_assets/maxwell.png"), self.baseSize)
        self.moyai3 = pg.transform.scale(pg.image.load("slots_assets/moyai.png"), self.baseSize)
        self.braindead2 = pg.transform.scale(pg.image.load("slots_assets/braindead.png"), self.baseSize)
        self.you1 = pg.transform.scale(pg.image.load("slots_assets/you.png"), self.baseSize)
        self.machine = pg.transform.scale(pg.image.load("slots_assets/machine.png"), (self.screen_width,self.screen_height))
        self.slot_items = [self.you1, self.braindead2, self.moyai3, self.maxwell4, self.ohNo5]
        self.lever = pg.Rect(1800, 1280, 350, 240)
        self.back = pg.Rect(self.screen_width-100, 0, 100, 100)
        self.win = False
        self.buttonActive = True

    def draw_objects(self):
        self.window.fill((151, 42, 39))
        self.window.blit(self.machine, (0,0))
        self.window.blit(self.backimg, (self.screen_width-100, 0))
        total_text = pg.font.Font(None, 200)
        self.window.blit(total_text.render(f"${self.starting_amount}", True, (0, 0, 0)), (500, 1350))

    def start_game(self):
        pg.draw.rect(self.window, (255, 0, 0), self.lever)
        pg.draw.rect(self.window, (0,0,0), self.back)
        self.draw_objects()
        self.window.blit(random.choice(self.slot_items), (379, 450))
        self.window.blit(random.choice(self.slot_items), (991, 450))
        self.window.blit(random.choice(self.slot_items), (1606, 450))
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONUP and self.buttonActive:
                    pos = pg.mouse.get_pos()
                    if self.back.collidepoint(pos):
                        start_main.start(self.starting_amount)
                    if self.lever.collidepoint(pos):
                        self.draw_objects()
                        self.game_logic()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_k:
                        if(self.win == True):
                            self.win = False
                        else:
                            self.win = True
            pg.display.update()

    def rollin(self):
        self.randRoll(.1)
        self.randRoll(.1)
        self.randRoll(.1)
        self.randRoll(.2)
        self.randRoll(.3)
        self.randRoll(.3)
        self.randRoll(.4)
        self.randRoll(.5)
        self.randRoll(.6)
        self.randRoll(.7)

    def randRoll(self, timer):
        self.draw_objects()
        self.window.blit(random.choice(self.slot_items), (379, 450))
        self.window.blit(random.choice(self.slot_items), (991, 450))
        self.window.blit(random.choice(self.slot_items), (1606, 450))
        pg.display.update()
        time.sleep(timer)

    def game_logic(self):
        if(self.starting_amount >= 25):
            self.buttonActive = False
            winnum = random.randint(0,100)
            self.starting_amount -= 25
            if(self.win):
                winnum = 100
            self.rollin()
            slot1 = random.choice(self.slot_items)
            slot2 = random.choice(self.slot_items)
            slot3 = random.choice(self.slot_items)
            if(winnum < 95):
                # lose scenario
                while(True):
                    if(slot1.get_parent == slot2.get_parent and slot2.get_parent == slot3.get_parent):
                        slot1 = random.choice(self.slot_items)
                        slot2 = random.choice(self.slot_items)
                        slot3 = random.choice(self.slot_items)
                    else:
                        break
            elif (winnum >= 95 and winnum < 97):
                self.starting_amount += 50
                slot1 = self.slot_items[0]
                slot2 = self.slot_items[0]
                slot3 = self.slot_items[0]
            elif (winnum == 97):
                self.starting_amount += 75
                slot1 = self.slot_items[1]
                slot2 = self.slot_items[1]
                slot3 = self.slot_items[1]
            elif (winnum == 98):
                self.starting_amount += 100
                slot1 = self.slot_items[2]
                slot2 = self.slot_items[2]
                slot3 = self.slot_items[2]
            elif (winnum == 99):
                self.starting_amount += 200
                slot1 = self.slot_items[3]
                slot2 = self.slot_items[3]
                slot3 = self.slot_items[3]
            elif (winnum == 100):
                self.starting_amount += 500
                slot1 = self.slot_items[4]
                slot2 = self.slot_items[4]
                slot3 = self.slot_items[4]
            self.draw_objects()
            self.window.blit(slot1, (379, 450))
            self.window.blit(slot2, (991, 450))
            self.window.blit(slot3, (1606, 450))
            self.buttonActive = True

if __name__ == "__main__":
    Slots().start_game()
