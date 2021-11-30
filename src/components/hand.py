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

    def evaluateHand(self):
        output = 0

        for card in self.cards:

            output += card.pip
        # Ace 11/1 conditional
            if output > 21:
                for ace in self.cards:
                    if ace.pip == 11:
                        ace.pip = 1
                        output -= 10
                    if output < 21:
                        break

        return output


    def clear(self):
        self.cards = []