import pygame, sys
from buttons.button import Button
from buttons.image_button import ImageButton
from buttons.text import Text
from components.card import CardComponent
from components.deckComponent import DeckComponent
from components.hand import HandComponent

BG_COLOR = (30, 30, 30)
BLACK_COLOR = (0, 0, 0)

def dealCards(deck, hand, n):
    for i in range(n):
        temp_card = deck.deal()

        hand.addCard(temp_card.suit, temp_card.name)


class BlackJackGame:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.can_bet = True
        self.setup_screen()
        self.won = False
        self.started = False
        self.stand_check = False
        self.deck = DeckComponent(self.screen, 240, 30)
        self.hand1 = HandComponent(self.screen, 200, 500)
        self.dealer_hand = HandComponent(self.screen, 200, 200)
        self.click = False
        self.running = True

        self.players = [self.hand1, self.dealer_hand]

        #blackjack table image
        self.bj_table = pygame.image.load('blackjackGame/assets/blackJackTable.png')
        self.bj_table =  pygame.transform.scale(self.bj_table, (800, 600))

        self.bet1 = 0
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
        self.current_bet1 = Text(self.screen, self.width - 150, self.height/2 + 100, f"Bank: ${self.bet1}")
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
        self.deck.draw()
        #self.hand1.draw()
        if not self.done_betting:
            self.button1.draw()
        #self.dealer_hand.draw()
        for hand in self.players:
            hand.draw()

        if self.stand_check:
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
            if self.chip500.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    self.bet1 += 500
                    self.current_bet1.setText(f"Current bet: {self.bet1}")
            elif self.chip100.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    self.bet1 += 100
                    self.current_bet1.setText(f"Current bet: {self.bet1}")
            elif self.chip50.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    self.bet1 += 50
                    self.current_bet1.setText(f"Current bet: {self.bet1}")
            elif self.chip25.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    self.bet1 += 25
                    self.current_bet1.setText(f"Current bet: {self.bet1}")
            elif self.chip1.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    self.bet1 += 1
                    self.current_bet1.setText(f"Current bet: {self.bet1}")
            if self.chip5.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    self.bet1 += 5
                    self.current_bet1.setText(f"Current bet: {self.bet1}")


            if self.button1.collides(pos) and self.click:
                if self.bet1 != 0:
                    self.done_betting = True

            if self.hit.collides(pos) and self.click:
                dealCards(self.deck, self.players[0], 1)

            if not self.stand_check and self.stand.collides(pos) and self.click:
                self.players[1].flipCard(1)
                self.stand_check = True
                player_val = self.players[0].evaluateHand()
                dealer_val = self.players[1].evaluateHand()
                while dealer_val < 17:
                    dealCards(self.deck, self.players[1], 1)
                    dealer_val = self.players[1].evaluateHand()
                if player_val > 21:
                    player_val = -1
                if dealer_val > 21:
                    dealer_val = -1
                if player_val > dealer_val:
                    self.status_text.setText("YOU WON!")

                elif player_val < dealer_val:
                    self.status_text.setText("YOU LOST!")
                else:
                    self.status_text.setText("Its a tie!")

            if not self.started and self.done_betting:

                dealCards(self.deck, self.players[0], 2)
                dealCards(self.deck, self.players[1], 2)

                self.players[1].flipCard(1)
                self.started = True
                val1 = self.players[0].evaluateHand()
                print(val1)

            if self.stand_check and self.new_hand.collides(pos) and self.click:
                self.players[0].clear()
                self.players[1].clear()
                self.started = False
                self.done_betting = False
                self.stand_check = False
                self.bet1 = 0
                self.current_bet1.setText(f"Current bet: {self.bet1}")
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