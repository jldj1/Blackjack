import pygame
ACTIVE_BG = (255, 255, 255)
INACTIVE_BG = (20, 20, 20)
FONT = pygame.font.SysFont("leelawadee", 20)

class InputBox:
    
    def __init__(self, screen, x, y, w, h, text=''):
        self.screen = screen
        self.rect = pygame.Rect(x, y, w, h)
        self.color = INACTIVE_BG
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # event pos is when the mouse was when the even happened
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
                
            self.color = ACTIVE_BG if self.active else INACTIVE_BG

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += str(event.unicode)
                
                # Re-render the text.=
                self.txt_surface = FONT.render(self.text, True, self.color)

    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text
        self.txt_surface = FONT.render(self.text, True, self.color)
    
    def draw(self):
        # draw text
        self.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # draw rectangle
        pygame.draw.rect(self.screen, self.color, self.rect, 2)