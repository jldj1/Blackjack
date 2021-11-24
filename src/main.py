import pygame, os
pygame.init()
# init pygame before importing other dependencies
# Jessie was here
from screens.auth_screen import AuthScreen
from blackjackGame.game import BlackjackGame

def main():
    auth_screen = AuthScreen()
    auth_screen.run()

if __name__ == "__main__":
    main()

#use lines 7- 18 in a home screen
game1 = BlackjackGame()

game1.addDealer([], 0)

#add players - stay in main
# while game1.total_players < 1:
#     new_player = input('Enter your name: ')
#     lang = input('Enter language: (en)glish, (es)pañol, (fr)ancais ')
#     game1.addPlayer(new_player, lang, 1000, 0, [], 0, 0)

#start new game
game1.startGame()

