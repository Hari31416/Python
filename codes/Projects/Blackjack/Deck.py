
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}

class Deck():
    
    def __init__(self):
        """Craeting the deck"""
        self.cards = []
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        print('Deck created!')
                
    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.cards)
        print("Deck shuffled!")
    
    def draw_cards(self):
        """Drawing a card"""
        print("\nDrawing one card and giving it to the: ")
        return self.cards.pop(0)
    
