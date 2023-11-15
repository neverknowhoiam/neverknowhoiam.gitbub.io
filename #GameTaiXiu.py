import random


def deposit():
    while True:
        balance = input('Enter your deposit: $')
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print('Deposit cannot less or equal to 0')
        else:
            print('Input value is not valid', end = ', ')
    return balance

def get_bet(balance):
    while True:
        bet = input('How much do you wanna bet? $')
        if bet.isdigit():
            bet = int(bet)
            if bet > (balance):
               print(f'Your bet ${bet} cannot greater than your balance ${balance}', end = ', ')
            else: 
                break
        else:
            print('Input value is not valid', end = ', ')  
    while True:
        player_choice = input('Which one do you want to bet on? (Tai or Xiu)-> ')
        if player_choice in ['Tai','Xiu']:
            break
        else:
            print('Choice is not valid.Please enter again', end = '\n' )
    return player_choice, bet 

def random_choice():
    result = []
    for _ in range(0,3):
        result.append(random.choice([1,2,3,4,5,6]))
    print(  result)
    return result

def game_work(balance):
    WON = False
    while True:
        TX_score = ''
        TX_result,bet = get_bet(balance)
        result = random_choice()
        balance -= bet
        if 3  <= sum(result) <=10:
            TX_score = 'Xiu'
        else:
            TX_score = 'Tai'
        print(f'Score: {sum(result)} -> {TX_score}')
        if  3  <= sum(result) <=10 and TX_result =='Xiu':
            WON = True
            balance += 1.5*bet
        elif 11 <= sum(result) <= 18 and TX_result =='Tai' :
            WON = True
            balance += 1.5*bet
        else:
            print(f'You lose! ${bet}. Your balance left ${balance}')
        if WON == True: 
            if len(set(result)) == 2 and TX_score == TX_result:
                balance += 2.5*bet
                
            elif len(set(result)) == 1 and TX_score == TX_result:
                balance += 4.5*bet
            print(f'You WIN!!! ${bet}. Your balance is ${balance}')
            print('Do you want to continue to play?\n')
        if balance == 0:
            print('You lose all your money!!')
            return balance
        return balance
    
def game_play():
    balance = deposit()
    newbalance = 0
    while True:
        if balance == 0:
            break
        else:
            play = input('Enter  to play (q to quit):')
            if play in ['q','Q']:
                print(f'You leave with your balance ${balance}')
                print('GAME EXIT!')
                break
            else:
                newbalance =game_work(balance)
                balance = newbalance
    return newbalance,balance 
game_play()