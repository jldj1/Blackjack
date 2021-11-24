import pygame, sys
from buttons.button import Button
from components.login_form import LoginForm
from screens.main_screen import MainScreen
from buttons.text import Text
BG_COLOR = (28, 170, 156)

BLACK_COLOR = (0, 0, 0)

class LoginScreen:
    def __init__(self):
        self.width = 600
        self.height = 600
        
        self.setup_screen()
        self.login_form = LoginForm(self.screen, 50, 300, 200, 45)
        self.user_label = Text(self.screen, 260, 303, "Enter Username")
        self.status_label = Text(self.screen, 50, 470, "", 25, (255, 0, 0))

        self.password_label = Text(self.screen, 260, 360, "Enter Password")
        self.click = False
        self.running = True
        # self, screen, x, y, width, height, text="", color=(DARK_GREY)
        self.go_back = Button(self.screen, 375, 530, 200, 50, "Go back", BLACK_COLOR)
        self.user_object = {}
        self.clock = pygame.time.Clock()


    def draw(self):
        self.screen.fill(BG_COLOR)
        # screen.fill always in beggining of draw func
        self.go_back.draw()
        self.login_form.draw()
        self.user_label.draw()
        self.password_label.draw()
        self.status_label.draw()
        # display.update() always in end of draw func
        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Login Screen")

    def run(self):
        while self.running: 
            pos = pygame.mouse.get_pos()
            print(pos)
            self.draw()
            if self.go_back.collides(pos) and self.click:
                self.running = False

            self.click = False
            for event in pygame.event.get():
                self.handle_event(event)

            self.clock.tick(60)


    def handle_event(self, event):
        self.user_object = self.login_form.handle_event(event)
        if "status" in self.user_object:
            status = self.user_object["status"]
            self.status_label.setText(status)

        if "success" in self.user_object:
            main_screen = MainScreen(self.user_object)
            main_screen.run()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                self.click = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()