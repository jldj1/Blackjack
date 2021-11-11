from components.card import CardComponent
import random
suits = ['spade', 'Heart', 'club', 'Diamond']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
pips = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}


class Card:
    def __init__(self, name, suit, pip):
        self.name = name
        self.pip = pip
        self.suit = suit


class DeckComponent:
    def __init__(self, screen, x, y):
        self.deck = self.createDeck()

        self.deck_image = CardComponent(screen, x, y, "club", 3)
        self.deck_image.flip()
        self.total_cards = len(self.deck)
        #self.hands = hands
        #self.total_players = len(hands)

    def createDeck(self):
        temp_deck = []
        for suit in suits:
            for card in cards:
                temp_card = Card(card, suit, pips[card])
                temp_deck.append(temp_card)

        random.shuffle(temp_deck)
        return temp_deck

    def draw(self):
        self.deck_image.draw()

    def deal(self):
        temp = self.deck.pop()
        self.total_cards -= 1
        return temp




