import random

# takes the users name (username)
username = input("Please enter your username: ")

f = open("player_data.txt", "r")
player_data = f.readlines()

if(username + "\n" not in player_data):
    f = open("player_data.txt", "a")
    f.write(f"\n{username}\n1000")
    f.close()

f = open("player_data.txt", "r")
player_data = f.readlines()
player_index = player_data.index(username + "\n")
balance_index = player_index + 1
player_balance = player_data[balance_index]

print(f"Hello! {username} Your blance is ${player_balance}")

#Takes the inital bet amount
bet = int(input("Enter Bet Amount: $"))
win_bet = bet * 2
double_win_bet = win_bet * 2

while(True):
    if(bet > int(player_balance)):
        print("Your bet amount has exceeded your current balance please enter a smaller amount.")
        print(f"Your blance is ${player_balance}")
        bet = int(input("Enter Bet Amount: $"))
    else:
        break

#Recods the dealers cards and values
dealer_cards = []
dealer_total_card_value = []
dealer_sum = 0
#Records the players cards and values
player_cards = []
player_total_card_value = []
player_sum = 0

cards = (1,2,3,4,5,6,7,8,9,10,11,12,13)

#Picks a random card from 13 possibilites and appends and prints it to the total (dealer_cards)
def generate_dealer_card():
    dealer = random.choice(cards)

    if(dealer == 1):
        dealer_cards.append("A")
        dealer_total_card_value.append(11)
    elif(dealer == 2):
        dealer_cards.append("2")   
        dealer_total_card_value.append(2)
    elif(dealer == 3):
        dealer_cards.append("3")  
        dealer_total_card_value.append(3) 
    elif(dealer == 4):
        dealer_cards.append("4")   
        dealer_total_card_value.append(4)
    elif(dealer == 5):
        dealer_cards.append("5")   
        dealer_total_card_value.append(5)
    elif(dealer == 6):
        dealer_cards.append("6")   
        dealer_total_card_value.append(6)
    elif(dealer == 7):
        dealer_cards.append("7")   
        dealer_total_card_value.append(7)
    elif(dealer == 8):
        dealer_cards.append("8")   
        dealer_total_card_value.append(8)
    elif(dealer == 9):
        dealer_cards.append("9")   
        dealer_total_card_value.append(9)
    elif(dealer == 10):
        dealer_cards.append("10")
        dealer_total_card_value.append(10)
    elif(dealer == 11):
        dealer_cards.append("J")   
        dealer_total_card_value.append(10)
    elif(dealer == 12):
        dealer_cards.append("Q")   
        dealer_total_card_value.append(10)
    else:
        dealer_cards.append("K")
        dealer_total_card_value.append(10)

generate_dealer_card()
dealer_sum = sum(dealer_total_card_value)

print(f'\nDealer First Card: {dealer_cards} Total: {dealer_sum}')

#Picks a random card from 13 possibilites and appends and prints it to the total (player_cards)
def generate_player_card():
    player = random.choice(cards)

    if(player == 1):
        player_cards.append("A")
        player_total_card_value.append(11)
    elif(player == 2):
        player_cards.append("2")   
        player_total_card_value.append(2)
    elif(player == 3):
        player_cards.append("3")  
        player_total_card_value.append(3) 
    elif(player == 4):
        player_cards.append("4")   
        player_total_card_value.append(4)
    elif(player == 5):  
        player_cards.append("5")   
        player_total_card_value.append(5)
    elif(player == 6):
        player_cards.append("6")   
        player_total_card_value.append(6)
    elif(player == 7):
        player_cards.append("7")   
        player_total_card_value.append(7)
    elif(player == 8):
        player_cards.append("8")   
        player_total_card_value.append(8)
    elif(player == 9):
        player_cards.append("9")   
        player_total_card_value.append(9)
    elif(player == 10):
        player_cards.append("10")
        player_total_card_value.append(10)
    elif(player == 11):
        player_cards.append("J")   
        player_total_card_value.append(10)
    elif(player == 12):
        player_cards.append("Q")   
        player_total_card_value.append(10)
    else:
        player_cards.append("K")
        player_total_card_value.append(10)

generate_player_card()
generate_player_card()
player_sum = sum(player_total_card_value)

print(f'\nPlayer Cards: {player_cards} Total: {player_sum}')

# choice menu
print('''\nPick from the following:
      1. Hit
      2. Stand
      3. Double
      4. Exit''')

while(True):
    choice = int(input("\nChoice: "))

    if(choice == 1):
        generate_player_card()
        player_sum = sum(player_total_card_value)

        for i in player_total_card_value:
            if(player_sum > 21) and (i == 11):
                player_sum = player_sum - 10
            
        if (player_sum >= 22):
            print("\nOutcome: Player has busted!")
            print(f"You have lost: ${bet}")

            player_data[balance_index]  = f'{int(player_balance) - bet}\n'
            with open('player_data.txt', 'w') as file:
                file.writelines(player_data)
            print(f"Your new balance is ${player_data[balance_index]}")
            break
        
        print(f'\nPlayer Cards: {player_cards} Total: {player_sum}')

    elif(choice == 2):
        generate_dealer_card()
        dealer_sum = sum(dealer_total_card_value)

        for i in dealer_total_card_value:
            if(dealer_sum > 21) and (i == 11):
                dealer_sum = dealer_sum - 10

        print(f'\nDealer Cards: {dealer_cards} Total: {dealer_sum}')
        print(f'\nPlayer Cards: {player_cards} Total: {player_sum}')
        
        if (dealer_sum <= 16):
            generate_dealer_card()
            dealer_sum = sum(dealer_total_card_value)
            print(f'\nDealer Cards: {dealer_cards} Total: {dealer_sum}')

        if(dealer_sum == player_sum):
            print("Outcome: Push")
            break
        elif(dealer_sum > player_sum) and (dealer_sum <= 21):
            print("\nOutcome: Player has lost!")
            print(f"You have lost: ${bet}")
            player_data[balance_index]  = f'{int(player_balance) - bet}\n'
            with open('player_data.txt', 'w') as file:
                file.writelines(player_data)
            print(f"Your new balance is ${player_data[balance_index]}")
            break
        elif(player_sum > dealer_sum ) and (player_sum <= 21):
            print("\nOutcome: Dealer has lost!")
            print(f"You have Won: ${win_bet}")  
            player_data[balance_index]  = f'{int(player_balance) + win_bet}\n'
            with open('player_data.txt', 'w') as file:
                file.writelines(player_data)
            print(f"Your new balance is ${player_data[balance_index]}")              
            break
        elif(dealer_sum >= 22):
            print("\nOutcome: Dealer has busted!")
            print(f"You have won: ${win_bet}")
            player_data[balance_index]  = f'{int(player_balance) + win_bet}\n'
            with open('player_data.txt', 'w') as file:
                file.writelines(player_data)
            print(f"Your new balance is ${player_data[balance_index]}")               
            break

    elif(choice == 3):
        generate_player_card()

        print(f"\nYour new bet is ${win_bet}")
        print(f'\nPlayer Cards: {player_cards} Total: {player_sum}')

        if (dealer_sum <= 16):
            generate_dealer_card()
            dealer_sum = sum(dealer_total_card_value)
            print(f'\nDealer Cards: {dealer_cards} Total: {dealer_sum}')

        if(dealer_sum > player_sum) and (dealer_sum <= 21):
            print("\nOutcome: Player has lost!")
            print(f"You have lost: ${bet}")
            player_data[balance_index]  = f'{int(player_balance) - bet}\n'
            with open('player_data.txt', 'w') as file:
                file.writelines(player_data)
            print(f"Your new balance is ${player_data[balance_index]}")
        elif(player_sum > dealer_sum ) and (player_sum <= 21):
            print("\nOutcome: Dealer has lost!")
            print(f"You have Won: ${double_win_bet}")   
            player_data[balance_index]  = f'{int(player_balance) + double_win_bet}\n'
            with open('player_data.txt', 'w') as file:
                file.writelines(player_data)
            print(f"Your new balance is ${player_data[balance_index]}")         
            break       
        elif(dealer_sum >= 22):
            print("\nOutcome: Dealer has busted!")
            print(f"You have won: ${double_win_bet}")
            player_data[balance_index]  = f'{int(player_balance) + double_win_bet}\n'
            with open('player_data.txt', 'w') as file:
                file.writelines(player_data)
            print(f"Your new balance is ${player_data[balance_index]}")         
    # exits the choice menu
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
