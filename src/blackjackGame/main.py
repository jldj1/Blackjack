#source: https://www.askpython.com/python/examples/blackjack-game-using-python

#import game class
from game import BlackjackGame

#new game
game1 = BlackjackGame()

game1.addDealer([], 0, 0)

#add players - stay in main
while game1.total_players < 1:
    new_player = input('Enter your name: ')
    lang = input('Enter language: (en)glish, (es)pañol, (fr)ancais ')
    game1.addPlayer(new_player, lang, 1000, 0, [], 0, 0, 0)

#start new game
game1.startGame()

#main game loop here
game1.run()

print('Thank you for playing!')