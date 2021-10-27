from buttons.text import Text
from buttons.square import TicTacToeBox

import socketio

import pygame

import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class TicTacToe:
    LINE_COLOR = (23, 145, 135)

    def __init__(self, screen, player_name, id=None):
        # 12323
        self.id = id or get_random_string(5)
    
        self.username = player_name
        self.sio = socketio.Client()
        self.setup()
        self.screen = screen
        self.rows = 3
        self.cols = 3
        self.board = []
        self.createBoard()

        self.round = 0
        self.id_text = Text(self.screen, 525, 0, self.id, 20)


    def createBoard(self):
        for i in range(self.rows):
            current_row = i * 200
            self.board.append([])
            for j in range(self.cols):
                current_col = j * 200
                self.board[i].append(TicTacToeBox(self.screen, current_col, current_row, 200, 200, "", color=(28, 170, 156)))

    def draw(self, click):
        for i in range(3):
            for j in range(3):
                if self.board[i][j].collides(pygame.mouse.get_pos()) and click:
                    if self.board[i][j].getValue() == "" and self.turn:
                        self.board[i][j].setValue(self.symbol)
                        self.round += 1
                        self.turn = False
                        self.send_data()

                self.board[i][j].draw()
        
        self.id_text.draw()

    def drawLines(self, WIDTH, HEIGHT):
        pygame.draw.line(self.screen, self.LINE_COLOR, (HEIGHT/3, 0), (WIDTH/3, HEIGHT), 10)
        pygame.draw.line(self.screen, self.LINE_COLOR, (HEIGHT/3 * 2, 0), (WIDTH/3 * 2, HEIGHT), 10)
        pygame.draw.line(self.screen, self.LINE_COLOR, (0, HEIGHT/3), (WIDTH, HEIGHT/3), 10)
        pygame.draw.line(self.screen, self.LINE_COLOR, (0, HEIGHT/3 * 2), (WIDTH, HEIGHT/3 * 2), 10)       

    def checkWinner(self, val):
        return 
    
    def send_data(self):
        temp_board = []
        
        for i in range(self.rows):
            temp_board.append([])
            for j in range(self.cols):
                temp_board[i].append(self.board[i][j].getValue())

        self.sio.emit('move', {'board': temp_board, "just_went": self.username, "channel": self.id})


    def normalize_data(self, raw_data):
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j].setValue(raw_data[i][j])

    def setup_callbacks(self):
        @self.sio.on("connect")
        def connect():
            print('connection established')
            
        @self.sio.on("disconnect")
        def disconnect():
            print('disconnected from server')
            self.sio.disconnect()
            # sio.eio.disconnect(True)

        @self.sio.on("move")
        def move_received(data):
            # game_state = data["response"]
            # print(game_state)
            print("data received")
            self.normalize_data(data["board"])
            
            if data["just_went"] == self.username:
                self.turn = False
            else:
                self.turn = True 


        @self.sio.on("sync_game")
        def update_players(data):
            print("player joined", data)
            
            players_dict = data["players"]
            
            # will return symbol of player
            self.symbol = players_dict[self.username]
            
            # will return all players in list format
            self.players = players_dict.keys()
            
            # if for some reason player did not join room successfully then 
            # server handled it by making the player a new room
            if self.id != data["channel"]:
                self.id = data["channel"]
                self.id_text = Text(self.screen, 525, 0, self.id, 20)
            
            # if your symbol is X when the game starts then you will go first
            self.turn = (self.symbol == "X") 


    def setup(self):
        self.setup_callbacks()
        # server ip
        self.sio.connect('http://127.0.0.1:5000')
        # when running local host switch to this
        # self.sio.connect('http://127.0.0.1:5000')
        
        # emit is the action sending to server
        self.sio.emit('join', {"player_name": self.username, "channel": self.id})

    def close_socket(self):
        self.sio.disconnect()