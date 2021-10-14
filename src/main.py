
import pygame

pygame.init()

from buttons.image_button import ImageButton

#screen, x, y, image_path, scale):

#### Create a canvas on which to display everything ####
window = (1150, 1050)
screen = pygame.display.set_mode(window)
#### Create a canvas on which to display everything ####

#### Create a surface with the same size as the window ####
background = pygame.Surface(window)
#### Create a surface with the same size as the window ####

#### Populate the surface with objects to be displayed ####
pygame.draw.rect(background,(0,255,255),(20,20,40,40))
pygame.draw.rect(background,(255,0,255),(120,120,50,50))
#### Populate the surface with objects to be displayed ####

table = pygame.image.load("images/table.jpg").convert_alpha()
table = pygame.transform.smoothscale(table, (1050, 1050))

hit = pygame.image.load("images/hit-hand-signal.gif").convert_alpha()
hit = pygame.transform.smoothscale(hit,(150,150))
stand = pygame.image.load("images/stand-sign.png").convert_alpha()
stand = pygame.transform.smoothscale(stand,(150, 150))




#### Blit the surface onto the canvas ####
screen.blit(background,(0,0))
#
screen.blit(table,(45,0))
screen.blit(hit,(80,650))
screen.blit(stand,(900,650))
image_button1 = ImageButton(screen, 500, 500, "cards/2_clover.png", 0.45)

#### Blit the surface onto the canvas ####

#### Update the the display and wait ####
pygame.display.flip()
done = False
while not done:
    image_button1.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#### Update the the display and wait ####
    pygame.display.update()
pygame.quit()
