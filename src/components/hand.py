from components.card import CardComponent

class HandComponent:
    
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.cards = []

    def addCard(self, suit, value):
        current_x = (len(self.cards) * 50) + self.x 
        new_card = CardComponent(self.screen, current_x, self.y, suit, value)
        self.cards.append(new_card)
        
    def draw(self):
        for card in self.cards:
            card.draw()
    
    def flipCard(self, index):
        self.cards[index].flip()

    def flipAll(self):
        for card in self.cards:
            card.flip()
