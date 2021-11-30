from components.deckComponent import DeckComponent
class TestBlackJack:
    def __init__(self, screen, player, dealer):
        self.screen = screen
        self.can_bet = True

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
        self.bet += bet
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

        elif player_val < dealer_val:
            output = "YOU LOST!"
        else:
            output = "Its a tie!"

        self.ended = True
        return output

    def hit(self):
        self.dealPlayer(1)

    def startRoundDeal(self):
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


