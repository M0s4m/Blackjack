import random

cards = (1,2,3,4,5,6,7,8,9,10,11,12,13)

dealerCards = []
dealerTotalCardValue = []
dealerSum = 0

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
generateDealerCard()
generateDealerCard()


# def calculateSum():
    # for i in dealerTotalCardValue:
        # dealerSum = dealerSum + i

