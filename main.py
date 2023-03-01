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
draw = ""
target = ""
investigatePlayer = ""
investigateCard = ""
#draw card
def drawCard():
    global draw
    draw = (random.choice(deck))
    deck.remove(draw)
#turn classes
def playerOneTurn():
    global currentPlayer
    global correctPlayer
    global playerOneName
    global target
    global investigatePlayer
    global investigateCard
    global playerTwoName
    global playerTwoHand
    global playerThreeHand
    global playerThreeName
    correctPlayerQuestion = ("Are you {name}? (Y/N) ")
    correctPlayer = input(correctPlayerQuestion.format(name = playerOneName))
    if correctPlayer == "y":
        currentPlayer = 1
        if playerOneName == "Player One":
            playerOneName = input("What is your name? ")
        print("Hand: ",playerOneHand)
        while investigatePlayer != playerOneName and investigatePlayer != playerTwoName:
            target = input("Which player do you want to investigate? 2 or 3? ")
            if target == 2 or target == "two" or target == playerTwoName:
                investigatePlayer = playerTwoName
            elif target == 3 or target == "three" or target == playerThreeName:
                investigatePlayer = playerThreeName
            else:
                print("I don't recognise that player")
        investigateCard = input("What card would you like to look for a partner for? ")
        if investigateCard in playerOneHand:
            print("Looking for ",investigateCard," in", investigatePlayer,"'s hand")
            if investigatePlayer == playerTwoName:
                if investigateCard in playerTwoHand:
                    #TODO: MAKE THIS WORK FOR SUITS OTHER THAN THE ONE IN YOUR HAND
                    print("You found it")
        else:
            print("That card isn't in your hand")
    else:
        print("Please pass the device to ",playerOneName)
        playerOneTurn()
        

#confirm windows OS
print("IMPORTANT: THIS WILL ONLY WORK ON WINDOWS MACHINES")
windowsConfirm = input("Are you either on windows or okay with the game breaking?(Yes/No) ")
if windowsConfirm == "yes":
    os.system('cls') 
    print("Game begining")
else:
    exit()
#Set up the game
currentPlayer = 1
for drawn in range(0,7):
    drawCard()
    playerOneHand.append(draw)
    drawCard()
    playerTwoHand.append(draw)
    drawCard()
    playerThreeHand.append(draw)
playerOneTurn()
