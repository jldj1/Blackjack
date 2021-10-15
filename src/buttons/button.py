import pygame

class Button:
    DARK_GREY = (29,29,29)

    def __init__(self, screen, x, y, width, height, text="", color=(DARK_GREY), hover=()):
        self.screen = screen 
        self.clicked = False

        self.height = height
        self.width = width
        self.text = text 
        self.color = color

        self.hover = (color[0] + 10, color[1] + 10, color[2] + 10)

        self.x = x
        self.y = y
        
        self.font = pygame.font.SysFont("leelawadee", 30)
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.topleft = (x, y)
        
    def collides(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self):
        color = self.color
        if self.collides(pygame.mouse.get_pos()):
            color = self.hover
        pygame.draw.rect(self.screen, color, self.rect)

        if len(self.text):
            text_img = self.font.render(self.text, True, (255,255,255))
            text_rect = text_img.get_rect(center=(self.rect.topleft[0] + (self.width // 2), self.rect.topleft[1] + (self.height // 2)))

            self.screen.blit(text_img, text_rect)
