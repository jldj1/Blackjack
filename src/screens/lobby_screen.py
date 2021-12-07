import pygame, sys
from buttons.button import Button
from screens.blackjackGame_screen import BlackJackGame
from pygame import mixer
BG_COLOR = (30, 30, 30)
BLACK_COLOR = (0, 0, 0)
import os
class LobbyScreen:
    def __init__(self, user):
        self.width = 600
        self.height = 600
        #12 - 14 and 4 to add sound anywhere. Just know where and what you want. so far mp3 works
        mixer.init()
        print(os.getcwd())
        mixer.music.load("sound_effects/login_sound.mp3")
        mixer.music.set_volume(1) #0- 1+ above one should be louder
        mixer.music.play()
        self.setup_screen()

        self.click = False
        self.running = True
        # self, screen, x, y, width, height, text="", color=(DARK_GREY)
        self.play_button = Button(self.screen, self.width//2 - 100, self.height//2 - 75, 200, 50, "Play Game", BLACK_COLOR)
        self.lobby_button = Button(self.screen, self.width // 2 - 100, self.height // 2 - 25, 200, 50, "lobby",BLACK_COLOR)
        self.clock = pygame.time.Clock()
        self.user = user

    def draw(self):
        self.screen.fill(BG_COLOR)
        # screen.fill always in beginning of draw func
        self.play_button.draw()
        self.lobby_button.draw()
        # display.update() always in end of draw func
        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Lobby Screen")

    def run(self):
        while self.running: 
            pos = pygame.mouse.get_pos()
            #print(pos)
            self.draw()
            if self.play_button.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")
                    blackjack_game = BlackJackGame(self.user)
                    blackjack_game.run()
                    #stats = blackjack_game.stats()
                    #stats_screen = StatsScreen(stats)
                    #stats_screen.run()


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