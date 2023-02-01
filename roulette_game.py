import pygame

class Bet:
    def __init__(self, amount, number = None, color = None, even = None, odd = None, range = None):
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
    
def start_game():
    pass