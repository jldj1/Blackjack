from components.deckComponent import DeckComponent
from network.users.users import UserModel
class TestBlackJack:
    # add balance
    def __init__(self, screen, player, dealer, username, users_balance):
        self.screen = screen
        self.username = username
        self.can_bet = True
        self.balance = int(users_balance)
        self.deck = DeckComponent(self.screen, 240, 30)
        self.won = False
        self.round_started = False
        self.stand_check = False
        self.ready_to_start_round = False
        self.started = False
        self.done_betting = False
        self.player = player
        self.dealer = dealer
        self.ended = False
        self.bet = 0


    def draw(self):
        self.deck.draw()

    def addBet(self, bet):
        #temp bet 200 + 100
        #balance: 100
        # 100 - 300
        #temp_bet = self.bet + bet
        #temp_balance = self.balance - bet
        #print("temp bet: " + str(temp_bet))
        if self.balance - bet < 0:
            return f"Current bet: {self.bet}"
        self.bet += bet
        self.balance = self.balance - bet

        self.ready_to_start_round = True
        return f"Current bet: {self.bet}"

    def dealPlayer(self, n):
        if not self.ended:
            for i in range(n):
                temp_card = self.deck.deal()
                self.player.addCard(temp_card.suit, temp_card.name)

    def dealDealer(self, n):
        if not self.ended:
            for i in range(n):
                temp_card = self.deck.deal()
                self.dealer.addCard(temp_card.suit, temp_card.name)

    def stand(self):
        if not self.started:
            return
        self.dealer.flipCard(1)
        self.stand_check = True

        player_val = self.player.evaluateHand()
        dealer_val = self.dealer.evaluateHand()

        while dealer_val < 17:
            self.dealDealer(1)
            dealer_val = self.dealer.evaluateHand()

        if player_val > 21:
            player_val = -1

        if dealer_val > 21:
            dealer_val = -1

        if player_val > dealer_val:
            output = "YOU WON!"

            self.balance = self.balance + self.bet * 2

        elif player_val < dealer_val:
            output = "YOU LOST!"
            #balance = self.balance - self.bet
        else:
            output = "Its a tie!"
            self.balance = self.balance + self.bet
        self.ended = True
        UserModel.save_user_info(self.username, self.balance)
        return output


    def hit(self):
        if not self.started:
            return
        self.dealPlayer(1)

    def startRoundDeal(self):
        if not self.ready_to_start_round:
            return
        self.dealDealer(2)
        self.dealPlayer(2)

        self.dealer.flipCard(1)

        self.started = True

    def reset(self):
        self.dealer.clear()
        self.player.clear()

        self.started = False
        self.done_betting = False
        self.stand_check = False
        self.bet = 0
        self.ended = False
        if self.deck.total_cards < 5:
            print("Shuffling...")
            self.deck = DeckComponent(self.screen, 240, 30)

    def getBalance(self):
        return self.balance

