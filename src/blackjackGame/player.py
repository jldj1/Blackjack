from deck import Deck


# class for new player
class Player:
    def __init__(self, name, lang, cash, score, hand, bet, bjState, ins):
        self.name = name
        self.cash = cash
        self.lang = lang
        self.hand = hand
        self.score = score
        self.bet = bet
        self.bjState = bjState
        self.ins = ins

    def setbj(self, state):
        self.bjState = state

    def getbj(self):
        return self.bjState

    def getName(self):
        return self.name

    def setBet(self, bet):
        if bet < self.cash:
            self.bet = bet
        else:
            return 'Insufficient funds!'

    def setIns(self, state):
        self.ins = state

    def insBet(self):
        insurance = input('Insurance? (y)es or (n)0?')
        if insurance == 'y':
            insBet = self.bet * 0.5
            if insBet < self.cash:
                self.cash -= insBet
            else:
                return 'Insufficient funds!'
        else:
            insBet = 0
            print('Insurance declined')
        return insBet

    def getBet(self):
        return self.bet

    def setCash(self):
        self.cash = self.cash

    def getCash(self):
        return self.cash

    def addCash(self, win):
        self.cash += win

    def minusCash(self):
        self.cash -= self.bet

    def resetScore(self):
        self.score = 0

    def setScore(self):
        self.score = self.score

    def getScore(self):
        return self.score

    def addScore(self):
        self.score += self.hand[-1][2]

        # Ace 11/1 conditional
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

    def getLang(self):
        return self.lang

    def setHand(self):
        # self.hand = []
        deal = Deck.deal()
        self.hand.append(deal)

    def getHand(self):
        # displayCards
        return self.hand
