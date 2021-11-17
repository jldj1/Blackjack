import pygame, sys
from buttons.button import Button
from buttons.image_button import ImageButton
from buttons.text import Text
from components.card import CardComponent
from components.deckComponent import DeckComponent
from components.hand import HandComponent

BG_COLOR = (30, 30, 30)
BLACK_COLOR = (0, 0, 0)

class BlackJackGame:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.can_bet = True
        self.setup_screen()



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

        #bank and bet area
        self.current_bet1 = Text(self.screen, self.width - 150, self.height/2 + 100, f"Bank: ${self.bet1}")
        self.clock = pygame.time.Clock()

        self.button1 = Button(self.screen, 300, 100, 200, 50, "Deal")

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
        self.button1.draw()
        #self.dealer_hand.draw()
        for hand in self.players:
            hand.draw()

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
                temp_card = self.deck.deal()
                #%
                index = self.deck.total_cards % len(self.players)
                print(index)

                self.players[index].addCard(temp_card.suit, temp_card.name)
                #self.hand1.addCard(temp_card.suit, temp_card.pip)


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