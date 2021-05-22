class Hand():
    def __init__(self):
        self.all_cards = []
        self.values_cards = []
        
    def add_to_hand(self):
        self.all_cards.append(deck.draw_cards())
        self.values_cards.append(self.all_cards[-1].value)
    
    def adjust_for_ace(self):
        return sum(self.values_cards)-10
    
    def value_hand(self):
        return sum(self.values_cards)
        
