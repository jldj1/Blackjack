import pygame, sys
from buttons.button import Button
from buttons.text import Text

BG_COLOR = (30, 30, 30)
BLACK_COLOR = (0, 0, 0)

class BlackJackGame:
    def __init__(self):
        self.width = 600
        self.height = 600
        
        self.setup_screen()

        self.click = False
        self.running = True

        self.bet1 = 0
        # self, screen, x, y, width, height, text="", color=(DARK_GREY)
        self.button = Button(self.screen, self.width//2 - 100, self.height//2 - 25, 200, 50, "bet", BLACK_COLOR)
        self.current_bet1 = Text(self.screen, 100, 100, "0")
        self.clock = pygame.time.Clock()


    def draw(self):
        self.screen.fill(BG_COLOR)
        # screen.fill always in beggining of draw func
        self.button.draw()
        self.current_bet1.draw()
        # display.update() always in end of draw func
        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Blank Template Screen")

    def run(self):
        while self.running: 
            pos = pygame.mouse.get_pos()
            print(pos)
            self.draw()
            if self.chip1.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    self.bet1 += 100
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