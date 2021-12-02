import pygame
import sys
from screens.lobby_screen import LobbyScreen

from buttons.image_button import ImageButton
from components.login_form import LoginForm
from components.register_form import RegisterForm
from buttons.text import Text

BG_COLOR = (28, 170, 156)

class MainScreen:

    def __init__(self, user):
        self.width = 745
        self.height = 500
        self.setup_screen()

        # objects init
        start_button = ImageButton(self.screen, 100, 200, "assets/start_btn.png", 0.7)
        exit_button = ImageButton(self.screen, 450, 200, "assets/exit_btn.png", 0.7)
        exit_button = ImageButton(self.screen, 450, 200, "assets/exit_btn.png", 0.7)
        user_text = Text(self.screen, 15, 15, "Not Logged in")
        balance_text = Text(self.screen, 15, 40, "")
        self.components = { "start": start_button, "exit": exit_button, "user_text": user_text, "balance_text": balance_text }


        self.click = False
        self.running = True

        # once user is logged in, user object will contain user information
        self.user_object = user
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill(BG_COLOR)

        for component in self.components.values():
            component.draw()
        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Menu")

    def run(self):
        while self.running:
            pos = pygame.mouse.get_pos()
            print(pos)

            self.draw()

            # if user successfully logged in
            if "success" in self.user_object:
                self.components["user_text"].setText(self.user_object["username"])
                self.components["balance_text"].setText("Balance: " + str(self.user_object["balance"]))

            if self.components["start"].collides(pos):
                if self.click:
                    LobbyScreen(self.user_object).run()
                    # self.setup_screen is to reset screen dimensions and window settings
                    # after the other window closes
                    self.setup_screen()

            if self.components["exit"].collides(pos):
                if self.click:
                    pygame.quit()
                    sys.exit()

            self.click = False
            for event in pygame.event.get():
                self.handle_event(event)

            self.clock.tick(60)

    def handle_event(self, event):
        # if not logged in yet
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.click = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()