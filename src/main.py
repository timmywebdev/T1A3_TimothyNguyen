import random
import time
from colorama import Fore

def reel():
    symbols = [ Fore.LIGHTCYAN_EX + 'J' + Fore.WHITE ,  Fore.LIGHTCYAN_EX + 'J' + Fore.WHITE ,  Fore.LIGHTCYAN_EX + 'J' + Fore.WHITE ,  Fore.LIGHTCYAN_EX + 'J' + Fore.WHITE ,  Fore.LIGHTCYAN_EX + 'J' + Fore.WHITE ,  
    Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, 
    Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, 
    Fore.LIGHTGREEN_EX + 'A' + Fore.WHITE, Fore.LIGHTGREEN_EX + 'A' + Fore.WHITE, Fore.LIGHTGREEN_EX + 'A' + Fore.WHITE, 
    Fore.LIGHTRED_EX + '8' + Fore.WHITE, Fore.LIGHTRED_EX + '8' + Fore.WHITE, 
    Fore.LIGHTCYAN_EX + '$' + Fore.WHITE]

    return random.choice(symbols)

def print_row(first, second, third):
    print('[ {} | {} | {} ]'.format(first, second, third,t=time.sleep(.15)), end='\r')

def round():
    for i in range(30):
        if i < 12:
            first = reel()
            second = reel()
            third = reel()

            print_row(first, second, third)
        elif i < 25:
            first = first
            second = reel()
            third = reel()

            print_row(first, second, third)
        else:
            first = first
            second = second
            third = reel()

            print_row(first, second, third)

    return (first, second, third)

def ask_to_play():
    global stake
    while(True):
        answer = input("You have £" + str(stake) + ". Would you like to play? y/n ")
        answer = answer.lower().strip()
        if(answer == "y"):
            return True
        elif(answer == "n"):
            print("You ended the game with £" + str(stake) + " in your hand.")
            return False
        else:
            print("incorrect input - type either y or n")

def check_win(a, b, c):
    if a == "$" and b == "$" and c == "$":
        Game.winnings = 1000*Game.current_bet
        print("\n\n *DING DING DING* JACKPOT!!!")
        press_to_continue()
    elif a == "8" and b == "8" and c == "8":
        Game.winnings = 888*Game.current_bet
        print("\n\n That is the Lucky888!")
        press_to_continue()
    elif a == "A" and b == "A" and c == "A":
        Game.winnings = 50*Game.current_bet
        print("\n\n You are an Ace")
        press_to_continue()
    elif a == "K" and b == "K" and c == "K":
        Game.winnings = 20*Game.current_bet
        press_to_continue()
        print("\n\n Eat and drink like a King!")
    elif a == "Q" and b == "Q" and c == "Q":
        Game.winnings = 10*Game.current_bet
        print("\n\n *YAAAS QUEEN!")
        press_to_continue()
    elif a == "J" and b == "J" and c == "J":
        Game.winnings = 5*Game.current_bet
        print("\n\n Jack of all trades!")
        press_to_continue()
    else:
        Game.winnings = 0

    if Game.winnings > 0:
        Game.credits += Game.winnings
        print(" Congratulations! You just won $" + str(Game.winnings) + "!!!")
    else:
        print("\n\n Sorry, no win this time.")
        press_to_continue()
        

def play():
    global stake
    want_to_play = ask_to_play()
    while(stake >= 1 and want_to_play == True):
        stake -= 1;
        round1 = round()
        a, b, c = round1
        print('[ {} | {} | {} ]'.format(a,b,c))
        check_win(a, b, c)
        
        if stake == 0:
            print("Sorry mate, you ran out of money!")
            break;
        
        
        want_to_play = ask_to_play()

stake = 20

play()