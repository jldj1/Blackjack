import pygame

class Text:
    def __init__(self, screen, x, y, text="", font_size=25, color=(255, 255, 255)):
        self.font = pygame.font.SysFont('leelawadee', font_size)
        self.screen = screen
        self.color = color
        self.text = text
        self.pos = (x, y)

    def setText(self, text):
        self.text = text

    def draw(self):
        textsurface = self.font.render(self.text, True, self.color)
        self.screen.blit(textsurface, self.pos)

