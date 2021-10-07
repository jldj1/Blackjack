import pygame
from buttons.button import Button

class ImageButton(Button):

    def __init__(self, screen, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        super().__init__(screen, x, y, width, height) 

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
