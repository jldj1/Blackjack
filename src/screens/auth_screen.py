import pygame, sys
from buttons.button import Button
from screens.auth_login import LoginScreen
from screens.auth_register import RegisterScreen

BG_COLOR = (28, 170, 156)
BLACK_COLOR = (0, 0, 0)

class AuthScreen:
    def __init__(self):
        self.width = 600
        self.height = 600
        
        self.setup_screen()

        self.click = False
        self.running = True
        # self, screen, x, y, width, height, text="", color=(DARK_GREY)
        padding = 60
        self.login_button = Button(self.screen, self.width // 2 - 100, self.height // 2 - 25, 200, 50, "Login", BLACK_COLOR)
        self.register_button = Button(self.screen, self.width // 2 - 100, self.height // 2 - 25 + padding, 200, 50, "Register", BLACK_COLOR)
        self.exit_button = Button(self.screen, self.width//2 - 100, self.height//2 - 25 + (padding * 2), 200, 50, "Exit", BLACK_COLOR)
        self.clock = pygame.time.Clock()


    def draw(self):
        self.screen.fill(BG_COLOR)
        # screen.fill always in beggining of draw func
        self.exit_button.draw()
        self.register_button.draw()
        self.login_button.draw()
        # display.update() always in end of draw func
        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("LOBBY")

    def run(self):
        while self.running: 
            pos = pygame.mouse.get_pos()
            print(pos)
            self.draw()

            if self.exit_button.collides(pos) and self.click:
                pygame.quit()
                sys.exit()

            if self.login_button.collides(pos) and self.click:
                login_screen = LoginScreen()
                login_screen.run()

            if self.register_button.collides(pos) and self.click:
                register_screen = RegisterScreen()
                register_screen.run()

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