import os
import random
deck = ["A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"]
playerOneName = ("Player One")
playerTwoName = ("Player Two")
playerThreeName = ("Player Three")
correctPlayer = ("N")
playerOneHand = []
playerTwoHand = []
playerThreeHand = []
currentPlayer = 0
draw = ("")
def drawCard():
    global draw
    draw = (random.choice(deck))
    deck.remove(draw)
    
def playerOneTurn():
    global currentPlayer
    global correctPlayer
    global playerOneName
    correctPlayer = input("Are you",playerOneName,"? (Y/N) ")
    if correctPlayer == "y":
        currentPlayer = 1
print("IMPORTANT: THIS WILL ONLY WORK ON WINDOWS MACHINES")
windowsConfirm = input("Are you either on windows or okay with the game breaking? ")
if windowsConfirm == "yes":
    os.system('cls') 
    print("Game begining")
else:
    exit
#Set up the game
currentPlayer = 1
