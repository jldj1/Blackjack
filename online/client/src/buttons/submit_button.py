# import pygame
# from buttons.button import Button
# class SubmitButton(Button):
#     def __init__(self, screen, x, y, w, h, text):
#         super().__init__(screen, x, y, w, h) 

#     def handle_event(self, event):
#         pos = pygame.mouse.get_pos()

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if self.collides(pos):
#                 self.submit()
    
#     def submit(self, username, password, api_function):
