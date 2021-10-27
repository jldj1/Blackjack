import pygame, sys
from buttons.button import Button
from components.card import CardComponent

from buttons.image_button import ImageButton

BG_COLOR = (30, 30, 30)
BLACK_COLOR = (0, 0, 0)

class Blank: 
    def __init__(self):
        self.width = 600
        self.height = 600
        
        self.setup_screen()

        self.click = False
        self.hold = False
        self.running = True
        
        # self, screen, x, y, width, height, text="", color=(DARK_GREY)
        self.flip_button = Button(self.screen, self.width//2 - 100, self.height//2 - 25, 200, 50, "flip card", BLACK_COLOR)
        
        
        # pos = pygame.mouse.get_pos()
        
        self.card1 = CardComponent(self.screen, 200, 50, "heart", 2)
        self.card2 = CardComponent(self.screen, 300, 50, "heart", 4)
        self.card3 = CardComponent(self.screen, 100, 100, "heart", 4)
        
        self.clock = pygame.time.Clock()


    def draw(self):
        self.screen.fill(BG_COLOR)
        # screen.fill always in beggining of draw func
        self.flip_button.draw()
        self.card1.draw()
        self.card2.draw()
        self.card3.draw()

            
        # display.update() always in end of draw func
        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Blank Template Screen")

    def run(self):
        while self.running: 
            pos = pygame.mouse.get_pos()
            print(pos)
            
            if self.card3.collides(pos) and self.click:
                self.card3.flipHold()
            
            if self.card3.getHold():
                self.card3.moveCard(pos[0], pos[1])
            
            self.draw()
            if self.flip_button.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    self.card2.flip()


            self.click = False
            for event in pygame.event.get():
                self.handle_event(event)

            self.clock.tick(60)


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