#source: https://www.askpython.com/python/examples/blackjack-game-using-python

#import game class
from game import BlackjackGame

#use lines 7- 18 in a home screen
game1 = BlackjackGame()

game1.addDealer([], 0)

#add players - stay in main
while game1.total_players < 1:
    new_player = input('Enter your name: ')
    lang = input('Enter language: (en)glish, (es)pañol, (fr)ancais ')
    game1.addPlayer(new_player, lang, 1000, 0, [], 0, 0)

#start new game
game1.startGame()

def setPlayerBet(player):
  #change text input to receive button input
  bet = int(input("Enter your bet: "))
  player.setBet(bet)

#begin main game loop here
while True:

  #ante - in run loop
  for name in game1.storage.keys():
      print(name, 'please enter your bet:')
      #bet = int(input())

      setPlayerBet(game1.storage[name])
      
      print('Bet: ')
      print(game1.storage[name].getBet())
      game1.storage[name].minusCash()
      print('New cash total: ')
      print(game1.storage[name].getCash())

  #first round deal players - in run loop
  for i in range(2):
    for name in game1.storage.keys():
      #add card to player hand
      game1.storage[name].setHand()
      #add player score
      game1.storage[name].addScore()
      #print player hand
      print(game1.storage[name].getName(), game1.storage[name].getHand(), game1.storage[name].getScore())

      #player natural (player has 21 after 2nd card)
      if game1.storage[name].getScore() == 21:
        print(game1.storage[name].getName(), "has Blackjack!")
        #set to blackjack (skip payout below)
        game1.storage[name].setbj(1)
        print(game1.storage[name].getbj())
        #payout for blackjack
        win = game1.storage[name].getBet() + (game1.storage[name].getBet() * 1.5)
        game1.storage[name].addCash(win)
        print("You won", win)
        print(game1.storage[name].getCash())

    #add card to dealer hand
    game1.dealer['Dealer'].setHand()
    #add dealer score
    game1.dealer['Dealer'].addScore()
    #print dealer hand
    if len(game1.dealer['Dealer'].getHand()) == 1:
      print(game1.dealer['Dealer'].card1(), game1.dealer['Dealer'].getScore())
    else:
      print('Dealer', game1.dealer['Dealer'].getHand(), game1.dealer['Dealer'].getScore())

  #dealer natural  
  if game1.dealer['Dealer'].getScore() == 21:
    print('Dealer has Blackjack!')
    #reset blackjack
    game1.storage[name].setbj(0)
    #reset player hand
    game1.storage[name].getHand().clear()
    print(game1.storage[name].getHand())
    #reset player score
    game1.storage[name].resetScore()
    print(game1.storage[name].getScore())
    #reset dealer hand/score
    game1.dealer['Dealer'].getHand().clear()
    print(game1.dealer['Dealer'].getHand()) 
    game1.dealer['Dealer'].resetScore()
    print(game1.dealer['Dealer'].getScore())  
    continue
    #add code to collect player bets

  #player hit/stay
  for name in game1.storage.keys():
    if game1.storage[name].getScore() == 21:
      continue
    if game1.storage[name].getScore() < 21:
      print(game1.storage[name].getName(), '(H)it/(S)tay:')
      hitStay = input()
    while hitStay.lower() != 's':
      #add card to player hand
      game1.storage[name].setHand()
      #add player score
      game1.storage[name].addScore()
      #print player hand
      print(game1.storage[name].getName(), game1.storage[name].getHand(), game1.storage[name].getScore())
      #ask hit/stay again?
      if game1.storage[name].getScore() < 21:
        print(game1.storage[name].getName(), '(H)it/(S)tay:')
        hitStay = input()
      #player reaches 21
      elif game1.storage[name].getScore() == 21:
        break    
      #player busts
      elif game1.storage[name].getScore() > 21:
        print(game1.storage[name].getName(), 'BUSTS!')
        break

  #dealer hit/stay on soft 17
  while game1.dealer['Dealer'].getScore() < 18 and 'A' in game1.dealer['Dealer'].getHand():
    game1.dealer['Dealer'].setHand()
    game1.dealer['Dealer'].addScore()

  #dealer stand on hard 17
  while game1.dealer['Dealer'].getScore() < 17:
    game1.dealer['Dealer'].setHand()
    game1.dealer['Dealer'].addScore()

  #print dealer hand
  print('Dealer', game1.dealer['Dealer'].getHand(), game1.dealer['Dealer'].getScore())

  #dealer bust conditional
  if game1.dealer['Dealer'].getScore() > 21:
    print('Dealer BUSTS!')

  #payouts/house take
  for name in game1.storage.keys():
    #player payout non-blackjack, dealer non-bust
    if game1.storage[name].getbj() == 0 and game1.storage[name].getScore() < 22:
      if game1.storage[name].getScore() > game1.dealer['Dealer'].getScore():
        win = game1.storage[name].getBet() * 2
        game1.storage[name].addCash(win)
        print(game1.storage[name].getName(), 'wins', win)
      #push
      if game1.storage[name].getScore() == game1.dealer['Dealer'].getScore():
        win = game1.storage[name].getBet()
        game1.storage[name].addCash(win)
        print('Push')
        print(game1.storage[name].getName(), game1.storage[name].getCash())

      #dealer bust
      if game1.dealer['Dealer'].getScore() > 21:
        win = game1.storage[name].getBet() * 2
        game1.storage[name].addCash(win)
        print(game1.storage[name].getName(), 'wins', win)
        print(game1.storage[name].getName(), game1.storage[name].getCash())

  replay = input('Play again? (y)es or (n)o')
  if replay.lower() == 'y':
    for name in game1.storage.keys():
      #reset blackjack
      game1.storage[name].setbj(0)
      #reset player hand
      game1.storage[name].getHand().clear()
      print(game1.storage[name].getHand())
      #reset player score
      game1.storage[name].resetScore()
      print(game1.storage[name].getScore())
    #reset dealer hand/score
    game1.dealer['Dealer'].getHand().clear()
    print(game1.dealer['Dealer'].getHand()) 
    game1.dealer['Dealer'].resetScore()
    print(game1.dealer['Dealer'].getScore())  
    continue
  else:
    break

print('Thank you for playing!')