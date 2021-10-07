import pygame, sys
from buttons.image_button import ImageButton
from game.tictactoe import TicTacToe 

pygame.init()

BG_COLOR = (28, 170, 156)
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

start_img = pygame.image.load("assets/start_btn.png").convert_alpha()
exit_img = pygame.image.load("assets/exit_btn.png").convert_alpha()

start_button = ImageButton(screen, 100, 200, start_img, 0.7)
exit_button = ImageButton(screen, 450, 200, exit_img, 0.7)

# screens below

def game():
    HEIGHT = 600
    WIDTH = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game1 = TicTacToe(screen)
    game1.createBoard()
    click = False
    running = True
    while running: 
        pygame.display.set_caption("Tic Tac Toe")
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(BG_COLOR)

        game1.drawBoard(click)
        
        game1.drawLines(WIDTH, HEIGHT)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


def main_menu():
    click = False
    run = True
    WIDTH = 800
    HEIGHT = 500
    while run: 

        pygame.display.set_caption("Duality Game")

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
        screen.fill(BG_COLOR)

        pos = pygame.mouse.get_pos()
        print(pos)
        start_button.draw()
        exit_button.draw()

        if start_button.collides(pos):
            if click:
                game()
        
        if exit_button.collides(pos):
            if click:
                pygame.quit()
                sys.exit()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    click = True

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

main_menu()