from blackjackGame.player import Player
from blackjackGame.dealer import Dealer

#class for game
class BlackjackGame:
    def __init__(self):
        self.storage = {}
        self.dealer = {}
        self.total_players = 0

    def addPlayer(self, player_name, cash, lang, hand, score, bet, bjState):
        if player_name not in self.storage:
            self.storage[player_name] = Player(player_name, cash, lang, hand, score, bet, bjState)
            self.total_players += 1
        return True

        return False
    
    def addDealer(self, hand, score):
      self.dealer['Dealer'] = Dealer([], 0)

    def getPlayerCash(self, name):
        return self.storage[name].getCash()

    def getAllPlayers(self):
        print(self.storage)

    def startGame(self):
        print('Dealer:', self.dealer['Dealer'].getHand(), self.dealer['Dealer'].getScore())
        for name, player_object in self.storage.items():
            print(name, player_object.getLang(), player_object.getCash(), player_object.getScore(),
                  player_object.getHand(), player_object.setbj(0))

    def run(self):
        pass