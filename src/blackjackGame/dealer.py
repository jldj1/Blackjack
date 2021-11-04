from deck import Deck

#class for dealer
class Dealer:
    def __init__(self, hand, score):
        self.hand = hand
        self.score = score
    #empty list for hand   
    #hand = []

    def setHand(self):
      #self.hand = []
      deal = Deck.deal()
      self.hand.append(deal)

    def card1(self):
      return "Dealer 1st card hidden"

    def getHand(self):
      return self.hand

    def addScore(self):
      self.score += self.hand[-1][2]

      #Ace 11/1 conditional
      if self.score > 21:
        for card in range(len(self.hand)):
          if self.hand[card][2] == 11:
            tempList = list(self.hand[card])
            print(tempList)
            tempList[2] = 1
            self.hand[card] = tuple(tempList)
            self.score -= 10


          if self.score < 21:
            break
    
    def resetScore(self):
      self.score = 0

    def setScore(self):
        self.score = self.score
    
    def getScore(self):
        return self.score
