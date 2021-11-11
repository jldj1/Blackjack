import pygame
from buttons.image_button import ImageButton

class CardComponent:
    def __init__(self, screen, x, y, suit, value):
            self.flipped = False
            self.value = value
            self.suit = suit
            
            card_image = f"blackjackGame/assets/Cards/{suit}_{value}.png"
            print("last card used:", card_image)
            self.card = ImageButton(screen, x, y, card_image, 0.5)   
            self.back = ImageButton(screen, x, y, "blackjackGame/assets/Cards/BackgroundRed.png", 0.5)
            
    def draw(self):
        if self.flipped == True:
            self.back.draw()
        else:
            self.card.draw()

    def flip(self):
        self.flipped = not self.flipped
    
    def getFlipped(self):
        return self.flipped
    