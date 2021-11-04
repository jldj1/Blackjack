import pygame
#from main import BlackjackGame, Player


class displayCards(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y, pic_path):
    super().__init__()
    self.image = pygame.image.load(pic_path)
    self.rect = self.image.get_rect()
    self.rect.center = [pos_x, pos_y]

  def update(self):
    pass

  
  def playerCards(self):
    pass






    

