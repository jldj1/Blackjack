import pygame, sys
from buttons.button import Button
from buttons.image_button import ImageButton
from buttons.text import Text

BG_COLOR = (30, 30, 30)
BLACK_COLOR = (0, 0, 0)

class BlackJackGame:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.can_bet = True
        
        self.setup_screen()

        self.click = False
        self.running = True

        #blackjack table image
        self.bj_table = pygame.image.load('blackjackGame/assets/blackJackTable.png')
        self.bj_table =  pygame.transform.scale(self.bj_table, (800, 600))

        self.bet1 = 0
        # self, screen, x, y, width, height, text="", color=(DARK_GREY)
        #chip buttons
        self.chip500 = ImageButton(self.screen, self.width - 300, self.height/2 + 100, 'blackjackGame/assets/Chips/chip500.png', 0.75)
        self.chip100 = ImageButton(self.screen, self.width - 300, self.height/2 + 200, 'blackjackGame/assets/Chips/chip100.png', 0.75)
        self.chip50 = ImageButton(self.screen, self.width - 200, self.height/2 + 100, 'blackjackGame/assets/Chips/chip50.png', 0.75)
        self.chip25 = ImageButton(self.screen, self.width - 200, self.height/2 + 200, 'blackjackGame/assets/Chips/chip25.png', 0.75)
        self.chip5 = ImageButton(self.screen, self.width - 100, self.height/2 + 100, 'blackjackGame/assets/Chips/chip5.png', 0.75)
        self.chip1 = ImageButton(self.screen, self.width - 100, self.height/2 + 200, 'blackjackGame/assets/Chips/chip1.png', 0.75)

        #bank and bet area
        self.current_bet1 = Text(self.screen, self.width - 200, self.height/2 + 60, f"Bank: ${self.bet1}")
        self.clock = pygame.time.Clock()



    def draw(self):
        self.screen.fill(BG_COLOR)
        # screen.fill always in beginning of draw func
        self.screen.blit(self.bj_table, (0, 0))
        #bank/bet area background
        pygame.draw.rect(self.screen, (65, 86, 127), pygame.Rect(self.width/2 + 100, self.height/2 + 100, 300, 200))
        pygame.draw.rect(self.screen, (65, 86, 127), pygame.Rect(self.width/2 + 190, self.height/2 + 50, 210, 50))
        self.chip500.draw()
        self.chip100.draw()
        self.chip50.draw()
        self.chip25.draw()
        self.chip5.draw()
        self.chip1.draw()
        self.current_bet1.draw()

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
            if self.chip500.collides(pos) and self.can_bet == True:
                if self.click:
                    print("BUTTON CLICKED")
                    self.bet1 += 500
                    #self.blackjack_game.setbet("chris", 200)
                    self.current_bet1.setText(f"Current bet: {self.bet1}")

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