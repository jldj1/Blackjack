from blackjackGame.player import Player
from blackjackGame.dealer import Dealer

# class for game
class BlackjackGame:
    def __init__(self):
        self.storage = {}
        self.dealer = {}
        self.total_players = 0

    def addPlayer(self, player_name, cash, lang, hand, score, bet, bjState, ins):
        if player_name not in self.storage:
            self.storage[player_name] = Player(player_name, cash, lang, hand, score, bet, bjState, ins)
            self.total_players += 1
        return True

        return False

    def addDealer(self, hand, score, take):
        self.dealer['Dealer'] = Dealer(hand, score, take)

    def getPlayerCash(self, name):
        return self.storage[name].getCash()

    def getAllPlayers(self):
        print(self.storage)

    def startGame(self):
        print('Dealer:', self.dealer['Dealer'].getHand(), self.dealer['Dealer'].getScore())
        for name, player_object in self.storage.items():
            print(name, player_object.getLang(), player_object.getCash(), player_object.getScore(),
                  player_object.getHand(), player_object.setbj(0))

    def replay(self):
        # change text input to receive button input
        for name in self.storage.keys():
            # reset blackjack
            self.storage[name].setbj(0)
            # reset player hand
            self.storage[name].getHand().clear()
            print(self.storage[name].getHand())
            # reset player score
            self.storage[name].resetScore()
            print(self.storage[name].getScore())
            # reset dealer hand/score/blackjack
            self.dealer['Dealer'].getHand().clear()
        print(self.dealer['Dealer'].getHand())
        self.dealer['Dealer'].resetScore()
        print(self.dealer['Dealer'].getScore())

    def run(self):
        while True:

            # ante - in run loop
            for name in self.storage.keys():
                # change text input to receive button input
                print(name, 'please enter your bet:')
                bet = int(input())

                self.storage[name].setBet(bet)

                print('Bet:', self.storage[name].getBet())
                self.storage[name].minusCash()
                print('New cash total:', self.storage[name].getCash())

            # first round deal players - in run loop
            for i in range(2):
                for name in self.storage.keys():
                    # add card to player hand
                    self.storage[name].setHand()
                    # add player score
                    self.storage[name].addScore()
                    # print player hand
                    print(self.storage[name].getName(), self.storage[name].getHand(), self.storage[name].getScore())

                    # player natural (player has 21 after 2nd card)
                    if self.storage[name].getScore() == 21:
                        print(self.storage[name].getName(), "has Blackjack!")
                        # set to blackjack (skip payout below)
                        self.storage[name].setbj(1)
                        print(self.storage[name].getbj())
                        # payout for blackjack
                        win = self.storage[name].getBet() + (self.storage[name].getBet() * 1.5)
                        self.storage[name].addCash(win)
                        print("You won", win)
                        print(self.storage[name].getCash())

                # add card to dealer hand
                self.dealer['Dealer'].setHand()
                # add dealer score
                self.dealer['Dealer'].addScore()
                # print dealer hand
                if len(self.dealer['Dealer'].getHand()) == 1:
                    print(self.dealer['Dealer'].card1(), self.dealer['Dealer'].getScore())
                else:
                    print('Dealer', self.dealer['Dealer'].getHand(), self.dealer['Dealer'].getScore())

            # insurance
            if self.dealer['Dealer'].card2() == 'A':
                for name in self.storage.keys():
                    self.storage[name].insBet()
                    if self.storage[name].insBet() > 0:
                        self.storage[name].setIns(1)
                # dealer natural
                if self.dealer['Dealer'].getScore() == 21:
                    print('Dealer has Blackjack!')
                    # player insurance payout
                    for name in self.storage.keys():
                        if self.storage[name].setIns == 1:
                            insWin = self.storage[name].getBet()
                            self.storage[name].addCash(insWin)
                            print("You won", insWin)
                            print(self.storage[name].getCash())

                        else:
                            take = self.storage[name].getBet()
                            self.dealer['Dealer'].setTake(take)
                            print(self.dealer['Dealer'].getTake())

                            # replay
                    replay = input('Play again? (y)es or (n)o: ')
                    if replay == 'y':
                        self.replay()
                        continue
                    else:
                        break
                else:
                    print('No blackjack.')

            # double down

            # player hit/stay
            for name in self.storage.keys():
                if self.storage[name].getScore() == 21:
                    continue
                if self.storage[name].getScore() < 21:
                    print(self.storage[name].getName(), '(H)it/(S)tay:')
                    hitStay = input()
                while hitStay.lower() != 's':
                    # add card to player hand
                    self.storage[name].setHand()
                    # add player score
                    self.storage[name].addScore()
                    # print player hand
                    print(self.storage[name].getName(), self.storage[name].getHand(), self.storage[name].getScore())
                    # ask hit/stay again?
                    if self.storage[name].getScore() < 21:
                        print(self.storage[name].getName(), '(H)it/(S)tay:')
                        hitStay = input()
                    # player reaches 21
                    elif self.storage[name].getScore() == 21:
                        break
                        # player busts
                    elif self.storage[name].getScore() > 21:
                        print(self.storage[name].getName(), 'BUSTS!')
                        break

            # conditional for dealer to stay if all players bust??
            for name in self.storage.keys():
                if self.storage[name].getScore() < 22:
                    # dealer hit/stay on soft 17
                    while self.dealer['Dealer'].getScore() < 18 and 'A' in self.dealer['Dealer'].getHand():
                        self.dealer['Dealer'].setHand()
                        self.dealer['Dealer'].addScore()

                    # dealer stand on hard 17
                    while self.dealer['Dealer'].getScore() < 17:
                        self.dealer['Dealer'].setHand()
                        self.dealer['Dealer'].addScore()

                    # print dealer hand
                    print('Dealer', self.dealer['Dealer'].getHand(), self.dealer['Dealer'].getScore())

                    break

            # player payouts/house take
            for name in self.storage.keys():
                # player payout non-blackjack, dealer non-bust
                if self.storage[name].getbj() == 0 and self.storage[name].getScore() < 22:
                    if self.storage[name].getScore() > self.dealer['Dealer'].getScore():
                        win = self.storage[name].getBet() * 2
                        self.storage[name].addCash(win)
                        print(self.storage[name].getName(), 'wins', win)
                        # dealer wins
                    elif self.dealer['Dealer'].getScore() < 22 and self.dealer['Dealer'].getScore() > self.storage[
                        name].getScore():
                        take = self.storage[name].getBet()
                        self.dealer['Dealer'].setTake(take)
                        print(self.dealer['Dealer'].getTake())
                        # push
                    elif self.storage[name].getScore() == self.dealer['Dealer'].getScore():
                        win = self.storage[name].getBet()
                        self.storage[name].addCash(win)
                        print('Push')
                        print(self.storage[name].getName(), self.storage[name].getCash())

                    # dealer bust
                    elif self.dealer['Dealer'].getScore() > 21:
                        print('Dealer BUSTS!')
                        win = self.storage[name].getBet() * 2
                        self.storage[name].addCash(win)
                        print(self.storage[name].getName(), 'wins', win)
                        print(self.storage[name].getName(), self.storage[name].getCash())

                # player bust
                if self.storage[name].getScore() > 21:
                    take = self.storage[name].getBet()
                    self.dealer['Dealer'].setTake(take)
                    print(self.dealer['Dealer'].getTake())

                    # replay
            replay = input('Play again? (y)es or (n)o: ')
            if replay == 'y':
                self.replay()
                continue
            else:
                break
