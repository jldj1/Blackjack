from random import choice

#class for deck of cards
class Deck():
    #deck = []
    def __init__(self, suits, cards, pips):
      #for card suit
      self.suits = suits

      #card type
      self.cards = cards

      #for numerical value
      self.pips = pips

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
    #deck of cards
    deck = []
    # add for loop for multi-shoe dec
    for suit in suits:
      for card in cards:
        deck.append((card, suit, pips[card]))

    def deal():
        card = choice(Deck.deck)
        Deck.deck.remove(card)
        return card

    def pipValue(self, deal):
      pip = deal[2]
      return pip