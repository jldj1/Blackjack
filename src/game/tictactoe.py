from buttons.square import TicTacToeBox
import pygame

class TicTacToe:
    LINE_COLOR = (23, 145, 135)

    def __init__(self, screen):
        self.turn = 0
        self.screen = screen
        self.rows = 3
        self.cols = 3
        self.board = []
        self.createBoard()

    def createBoard(self):
        for i in range(self.rows):
            current_row = i * 200
            self.board.append([])
            for j in range(self.cols):
                current_col = j * 200
                self.board[i].append(TicTacToeBox(self.screen, current_col, current_row, 200, 200, "", color=(28, 170, 156)))
    
    def drawBoard(self, click):
        for i in range(3):
            for j in range(3):
                if self.board[i][j].collides(pygame.mouse.get_pos()) and click:
                    if self.board[i][j].getValue() == "":
                        self.board[i][j].setValue(self.getCurrentTurnValue())
                        self.nextTurn()
                self.board[i][j].draw()

    def getCurrentTurnValue(self):
        if self.turn:
            return "O"
        else: 
            return "X"

    def nextTurn(self):
        self.turn = not self.turn

    def drawLines(self, WIDTH, HEIGHT):
        pygame.draw.line(self.screen, self.LINE_COLOR, (HEIGHT/3, 0), (WIDTH/3, HEIGHT), 10)
        pygame.draw.line(self.screen, self.LINE_COLOR, (HEIGHT/3 * 2, 0), (WIDTH/3 * 2, HEIGHT), 10)
        pygame.draw.line(self.screen, self.LINE_COLOR, (0, HEIGHT/3), (WIDTH, HEIGHT/3), 10)
        pygame.draw.line(self.screen, self.LINE_COLOR, (0, HEIGHT/3 * 2), (WIDTH, HEIGHT/3 * 2), 10)       

    def checkWinner(self, val):
        pass
    