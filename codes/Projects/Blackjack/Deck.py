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
    
