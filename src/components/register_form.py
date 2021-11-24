import pygame
from buttons.button import Button
from buttons.input_box import InputBox
from network.users.users import UserModel


# Register Form component holds three elements, 
#  3 Boxes email, username, password
# 1 Button

class RegisterForm:
    def __init__(self, screen, x, y, w, h):
        self.screen = screen
        padding = h + 10
        self.email_box = InputBox(screen,x, y, w, h)
        self.user_box = InputBox(screen, x, y + padding, w, h)
        self.pass_box = InputBox(screen, x, y + padding * 2, w, h)
        self.button = Button(screen, x, y + padding * 3, w, h, "Register")
        self.logout_button = Button(screen, x, y, w, h, "Submit")

        self.status = {}
        
    def handle_event(self, event):
        self.email_box.handle_event(event)
        self.user_box.handle_event(event)
        self.pass_box.handle_event(event)

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.status:
                if self.button.collides(pos):
                    self.status = self.submit()

        return self.status

    def draw(self):
        # draw three elements at once email, username, password
        #if not self.status:
        self.button.draw()
        self.email_box.draw()
        self.user_box.draw()
        self.pass_box.draw()

    def submit(self):
        email = self.email_box.getText()
        username = self.user_box.getText()
        password = self.pass_box.getText()

        response = UserModel.create_user(email, username, password)
        self.email_box.setText("")
        self.user_box.setText("")
        self.pass_box.setText("")

        if "error" in response:
            return {}
        else:
            return response
