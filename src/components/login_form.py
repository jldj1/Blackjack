import pygame
from buttons.button import Button
from buttons.input_box import InputBox
from network.users.users import UserModel

padding = 10

# Login Form component holds three elements, 
# 2 Input Boxes
# 1 Button

class LoginForm:
    def __init__(self, screen, x, y, w, h):
        self.screen = screen
        self.user_box = InputBox(screen, x, y, w, h)
        self.pass_box = InputBox(screen, x, y + h + padding, w, h)
        self.button = Button(screen, x, y + h * 2 + padding + 10, w, h, "Login")
        self.status = {}
        
    def handle_event(self, event):
        self.user_box.handle_event(event)
        self.pass_box.handle_event(event)

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.collides(pos):
                self.status = self.submit()
        
        return self.status

    def draw(self):
        # draw three elements at once
        self.button.draw()
        self.user_box.draw()
        self.pass_box.draw()


    def submit(self):
        username = self.user_box.getText()
        password = self.pass_box.getText()
        response = UserModel.authenticate(username, password)

        self.user_box.setText("")
        self.pass_box.setText("")

        if "error" in response:
            return {}
        else:
            return response
