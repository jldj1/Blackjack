import pygame, sys
from buttons.button import Button
from buttons.image_button import ImageButton
from buttons.text import Text
from components.card import CardComponent
from components.deckComponent import DeckComponent
from components.hand import HandComponent
from components.testblackjack import TestBlackJack

BG_COLOR = (30, 30, 30)
BLACK_COLOR = (0, 0, 0)

def dealCards(deck, hand, n):
    for i in range(n):
        temp_card = deck.deal()
        hand.addCard(temp_card.suit, temp_card.name)


class BlackJackGame:
    def __init__(self, user):
        self.user = user
        self.width = 800
        self.height = 600
        self.setup_screen()
        self.hand1 = HandComponent(self.screen, 200, 500)
        self.dealer_hand = HandComponent(self.screen, 200, 200)
        self.usernamelabel = Text(self.screen, 5, 15, f"{user['username']}")
        self.balancelabel = Text(self.screen, 5, 35, f"Balance:{user['balance']}")
        self.game = TestBlackJack(self.screen, self.hand1, self.dealer_hand, user["username"],  user["balance"])

        self.click = False
        self.running = True

        self.players = [self.hand1, self.dealer_hand]

        #blackjack table image
        self.bj_table = pygame.image.load('blackjackGame/assets/blackJackTable.png')
        self.bj_table =  pygame.transform.scale(self.bj_table, (800, 600))
        # self, screen, x, y, width, height, text="", color=(DARK_GREY)
        #chip buttons
        self.chip500 = ImageButton(self.screen,  670, 415, 'blackjackGame/assets/Chips/chip500.png', 0.45)
        self.chip100 = ImageButton(self.screen, 740, 415, 'blackjackGame/assets/Chips/chip100.png', 0.45)
        self.chip50 = ImageButton(self.screen, 670, 465, 'blackjackGame/assets/Chips/chip50.png', 0.45)
        self.chip25 = ImageButton(self.screen,  740, 465, 'blackjackGame/assets/Chips/chip25.png', 0.45)
        self.chip5 = ImageButton(self.screen,  670, 510, 'blackjackGame/assets/Chips/chip5.png', 0.45)
        self.chip1 = ImageButton(self.screen,  740, 510, 'blackjackGame/assets/Chips/chip1.png', 0.45)
        self.new_hand = Button(self.screen, 300, 100, 200, 50, "New Hand")
        #bank and bet area
        self.current_bet1 = Text(self.screen, self.width - 150, self.height/2 + 100, f"Bank: $0")
        self.clock = pygame.time.Clock()
        self.status_text = Text(self.screen, 100, 100, "")
        self.button1 = Button(self.screen, 300, 100, 200, 50, "Deal")
        self.done_betting = False
        self.hit = ImageButton(self.screen, 20, 400, 'assets/imgs/hit-hand-signal.gif', 0.45)
        self.stand = ImageButton(self.screen, 20, 500, 'assets/imgs/stand-sign.png', 0.19)

    def draw(self):
        self.screen.fill(BG_COLOR)
        # screen.fill always in beginning of draw func
        self.screen.blit(self.bj_table, (0, 0))
        self.usernamelabel.draw()
        self.balancelabel.draw()
        #bank/bet area background
        pygame.draw.rect(self.screen, (65, 86, 127), pygame.Rect(640, 390, 300, 200))
        #pygame.draw.rect(self.screen, (65, 86, 127), pygame.Rect(self.width/2 + 190, self.height/2 + 50, 210, 50))
        self.chip500.draw()
        self.chip100.draw()
        self.chip50.draw()
        self.chip25.draw()
        self.chip5.draw()
        self.chip1.draw()
        self.current_bet1.draw()
        self.game.draw()


        #self.hand1.draw()
        if not self.game.done_betting:
            self.button1.draw()
        #self.dealer_hand.draw()
        for hand in self.players:
            hand.draw()

        if self.game.stand_check:
            self.status_text.draw()
            self.new_hand.draw()

        self.hit.draw()
        self.stand.draw()
        # display.update() always in end of draw func
        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Blank Template Screen")

    def run(self):
        while self.running: 
            pos = pygame.mouse.get_pos()
            #print(pos)
            self.draw()
            #set bets
            if self.chip500.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    #self.bet1 += 500
                    text = self.game.addBet(500)
                    # self.game.addBet(500)
                    self.current_bet1.setText(text)

            elif self.chip100.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    text = self.game.addBet(100)
                    self.current_bet1.setText(text)
            elif self.chip50.collides(pos):
                if self.click:
                    text = self.game.addBet(50)
                    self.current_bet1.setText(text)
            elif self.chip25.collides(pos):
                if self.click:
                    text = self.game.addBet(25)
                    self.current_bet1.setText(text)
            elif self.chip1.collides(pos):
                if self.click:
                    text = self.game.addBet(1)
                    self.current_bet1.setText(text)
            if self.chip5.collides(pos):
                if self.click:
                    text = self.game.addBet(5)
                    self.current_bet1.setText(text)


            self.balancelabel.setText(f"Balance: {self.game.getBalance()}")
            if self.button1.collides(pos) and self.click and self.game.ready_to_start_round:
                self.game.startRoundDeal()
                value1 = self.hand1.evaluateHand()

                if value1 == 21:
                    text = self.game.stand()
                    self.status_text.setText("BLACKJACK!")

            if self.hit.collides(pos) and self.click:
                self.game.hit()

            if not self.game.stand_check and self.stand.collides(pos) and self.click:
                text = self.game.stand()
                print(text)
                self.status_text.setText(text)

            if self.game.stand_check and self.new_hand.collides(pos) and self.click:
                self.game.reset()

                self.current_bet1.setText(f"Current bet: {self.game.bet}")
                self.status_text.setText("")

            self.click = False
            for event in pygame.event.get():
                self.handle_event(event)

            self.clock.tick(60)

            #game play logic (bet, card deal, hit/stay, win/lose)


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                self.click = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()