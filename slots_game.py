import pygame as pg
import sys
import random
import pyautogui
import time
import start_main

# set the game screen  

screen_width, screen_height = pyautogui.size()
pg.init()
pg.display.set_caption("Slots")
baseSize = (550,600)

window = None
backimg = pg.image.load("slots_assets/back.png")
ohNo5 = pg.transform.scale(pg.image.load("slots_assets/ohno.png"), baseSize)
maxwell4 = pg.transform.scale(pg.image.load("slots_assets/maxwell.png"), baseSize)
moyai3 = pg.transform.scale(pg.image.load("slots_assets/moyai.png"), baseSize)
braindead2 = pg.transform.scale(pg.image.load("slots_assets/braindead.png"), baseSize)
you1 = pg.transform.scale(pg.image.load("slots_assets/you.png"), baseSize)
machine = pg.transform.scale(pg.image.load("slots_assets/machine.png"), (screen_width,screen_height))

slot_items = [you1, braindead2, moyai3, maxwell4, ohNo5]

lever = pg.Rect(1800, 1280, 350, 240) # , , length height
back = pg.Rect(screen_width-100, 0, 100, 100)
window = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)
global buttonActive
win = False
buttonActive = True

def draw_objects():
    window.fill((151, 42, 39))  # fill with color    
    window.blit(machine, (0,0))  # fill with color
    window.blit(backimg, (screen_width-100, 0))

def start_game():
    global win
    pg.draw.rect(window, (255, 0, 0), lever)
    pg.draw.rect(window, (0,0,0), back)
    draw_objects()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP and buttonActive:
                pos = pg.mouse.get_pos()
                if back.collidepoint(pos):
                    start_main.start()
                if lever.collidepoint(pos):
                    draw_objects()
                    game_logic()
            if event.type == pg.KEYUP:
                if event.key == pg.K_k:
                    if(win == True):
                        win = False
                    else:
                        win = True
        pg.display.update()

def rollin():
    randRoll(.1)
    randRoll(.1)
    randRoll(.1)
    randRoll(.2)
    randRoll(.3)
    randRoll(.3)
    randRoll(.4)
    randRoll(.5)
    randRoll(.6)
    randRoll(.7)
    draw_objects()

def randRoll(timer):
    draw_objects()
    window.blit(random.choice(slot_items), (393, 500))
    window.blit(random.choice(slot_items), (985, 500))
    window.blit(random.choice(slot_items), (1605, 500))
    pg.display.update()
    time.sleep(timer)

def game_logic():
    buttonActive = False
    winnum = random.randint(0,100)
    if(win):
        winnum = 100
    rollin()
    slot1 = random.choice(slot_items)
    slot2 = random.choice(slot_items)
    slot3 = random.choice(slot_items)
    if(winnum < 95):
        # lose scenario
        while(True):
            if(slot1.get_parent == slot2.get_parent and slot2.get_parent == slot3.get_parent):
                slot1 = random.choice(slot_items)
                slot2 = random.choice(slot_items)
                slot3 = random.choice(slot_items)
            else:
                break
    elif (winnum >= 95 and winnum < 97):
        slot1 = slot_items[0]
        slot2 = slot_items[0]
        slot3 = slot_items[0]
    elif (winnum == 97):
        slot1 = slot_items[1]
        slot2 = slot_items[1]
        slot3 = slot_items[1]
    elif (winnum == 98):
        slot1 = slot_items[2]
        slot2 = slot_items[2]
        slot3 = slot_items[2]
    elif (winnum == 99):
        slot1 = slot_items[3]
        slot2 = slot_items[3]
        slot3 = slot_items[3]
    elif (winnum == 100):
        slot1 = slot_items[4]
        slot2 = slot_items[4]
        slot3 = slot_items[4]
    window.blit(slot1, (393, 500))
    window.blit(slot2, (985, 500))
    window.blit(slot3, (1605, 500))
    buttonActive = True


if __name__ == "__main__":
    start_game()
