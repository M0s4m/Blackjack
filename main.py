import random

#Takes the inital bet amount
bet = int(input("Enter Bet Amount: $"))

#Recods the dealers cards and values
dealerCards = []
dealerTotalCardValue = []
dealerSum = 0
#Records the players cards and values
playerCards = []
playerTotalCardValue = []
playerSum = 0

# suits = (0,1,2,3)
cards = (1,2,3,4,5,6,7,8,9,10,11,12,13)

#Picks a random card from 13 possibilites and appends and prints it to the total (dealerCards)
def generateDealerCard():
    dealer = random.choice(cards)

    if(dealer == 1):
        dealerCards.append("A")
        dealerTotalCardValue.append(1)
    elif(dealer == 2):
        dealerCards.append("2")   
        dealerTotalCardValue.append(2)
    elif(dealer == 3):
        dealerCards.append("3")  
        dealerTotalCardValue.append(3) 
    elif(dealer == 4):
        dealerCards.append("4")   
        dealerTotalCardValue.append(4)
    elif(dealer == 5):
        dealerCards.append("5")   
        dealerTotalCardValue.append(5)
    elif(dealer == 6):
        dealerCards.append("6")   
        dealerTotalCardValue.append(6)
    elif(dealer == 7):
        dealerCards.append("7")   
        dealerTotalCardValue.append(7)
    elif(dealer == 8):
        dealerCards.append("8")   
        dealerTotalCardValue.append(8)
    elif(dealer == 9):
        dealerCards.append("9")   
        dealerTotalCardValue.append(9)
    elif(dealer == 10):
        dealerCards.append("10")
        dealerTotalCardValue.append(10)
    elif(dealer == 11):
        dealerCards.append("J")   
        dealerTotalCardValue.append(10)
    elif(dealer == 12):
        dealerCards.append("Q")   
        dealerTotalCardValue.append(10)
    else:
        dealerCards.append("K")
        dealerTotalCardValue.append(10)

generateDealerCard()

for i in dealerTotalCardValue:
    dealerSum = dealerSum + i

print(f'\nDealer First Card: {dealerCards} Total: {dealerSum}')

#Picks a random card from 13 possibilites and appends and prints it to the total (playerCards)
def generatePlayerCard():
    player = random.choice(cards)

    if(player == 1):
        playerCards.append("A")
        playerTotalCardValue.append(1)
    elif(player == 2):
        playerCards.append("2")   
        playerTotalCardValue.append(2)
    elif(player == 3):
        playerCards.append("3")  
        playerTotalCardValue.append(3) 
    elif(player == 4):
        playerCards.append("4")   
        playerTotalCardValue.append(4)
    elif(player == 5):  
        playerCards.append("5")   
        playerTotalCardValue.append(5)
    elif(player == 6):
        playerCards.append("6")   
        playerTotalCardValue.append(6)
    elif(player == 7):
        playerCards.append("7")   
        playerTotalCardValue.append(7)
    elif(player == 8):
        playerCards.append("8")   
        playerTotalCardValue.append(8)
    elif(player == 9):
        playerCards.append("9")   
        playerTotalCardValue.append(9)
    elif(player == 10):
        playerCards.append("10")
        playerTotalCardValue.append(10)
    elif(player == 11):
        playerCards.append("J")   
        playerTotalCardValue.append(10)
    elif(player == 12):
        playerCards.append("Q")   
        playerTotalCardValue.append(10)
    else:
        playerCards.append("K")
        playerTotalCardValue.append(10)

generatePlayerCard()
generatePlayerCard()

for i in playerTotalCardValue:
    playerSum = playerSum + i

print(f'\nPlayer Cards: {playerCards} Total: {playerSum}')

#Choice menu
print('''\nPick from the following:
      1. Hit
      2. Stand
      3. Double
      4. Exit''')

while(True):
    choice = int(input("\nChoice: "))
    #Gives the player another card
    if(choice == 1):

        player = random.choice(cards)
        playerCards.append(player)

        print(f'Player Cards: {playerCards} Total: {playerSum}')

    #Reveals the dealers second card
    elif(choice == 2):

        dealer = random.choice(cards)
        dealerCards.append(dealer)

        print(f'\nDealer Cards: {dealerCards} Total: {dealerSum}')
        print(f'\nPlayer Cards: {playerCards} Total: {playerSum}')

    #Doubles the bet, Reveals the dealers second card, Gives the player another card
    elif(choice == 3):

        player = random.choice(cards)
        playerCards.append(player)

        doubleBet = bet * 2

        dealer = random.choice(cards)
        dealerCards.append(dealer)

        print(f'\nDealer Cards: {dealerCards} Total: {dealerSum}')   
        print(f'\nNew bet: ${doubleBet}')
        print(f'Player Cards: {playerCards} Total: {playerSum}')

    #Exits the choice menu
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")