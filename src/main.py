import random
import time
import os
import colorama
from colorama import Fore

class Game:
    current_bet = 0
    winnings = 0
    credits = 0

def reel_randomiser():
    symbols = [ Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE , Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE , Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE , Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE , Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE , 
    Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, 
    Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, 
    Fore.LIGHTGREEN_EX + 'A' + Fore.WHITE, Fore.LIGHTGREEN_EX + 'A' + Fore.WHITE, Fore.LIGHTGREEN_EX + 'A' + Fore.WHITE, 
    Fore.LIGHTRED_EX + '8' + Fore.WHITE, Fore.LIGHTRED_EX + '8' + Fore.WHITE, 
    Fore.LIGHTCYAN_EX + '$' + Fore.WHITE]

    return random.choice(symbols)

def spinning(a, b, c):
    print('\t\t   ------> | {} | {} | {} | <------'.format(a, b, c,t=time.sleep(.15)), end='\r')

def press_to_continue():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n Press any key to continue...\"'")
    os.system('clear')
    print()

def spin_anim():
    for i in range(30):
        if i < 12:
            first = reel_randomiser()
            second = reel_randomiser()
            third = reel_randomiser()

            spinning(first, second, third)
        elif i < 25:
            first = first
            second = reel_randomiser()
            third = reel_randomiser()

            spinning(first, second, third)
        else:
            first = first
            second = second
            third = reel_randomiser()

            spinning(first, second, third)

    return (first, second, third)

def reel():
    symbols = [ Fore.LIGHTBLUE_EX + 'JJJJJ', Fore.LIGHTMAGENTA_EX + 'QQQQQ', Fore.LIGHTYELLOW_EX + 'KKKKK', Fore.LIGHTGREEN_EX + 'AAA', Fore.LIGHTRED_EX + '88', Fore.LIGHTMAGENTA_EX + '$']
    return random.choice(symbols)

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