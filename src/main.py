import random
import time
import os
from colorama import Fore

class Game:
    current_bet = 0
    winnings = 0
    credits = 0

class Items:
    jack = Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE
    queen = Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE
    king = Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE
    ace =  Fore.LIGHTGREEN_EX + 'A' + Fore.WHITE
    lucky888 =  Fore.LIGHTRED_EX + '8' + Fore.WHITE
    jackpot = Fore.LIGHTCYAN_EX + '$' + Fore.WHITE

    jack_value = 50
    queen_value = 75
    king_value = 100
    ace_value = 200
    lucky888_value = 8888
    jackpot_value = 10000

def reel_randomiser():
    symbols = [Items.jack, Items.jack, Items.jack, Items.jack, Items.jack,
    Items.queen, Items.queen, Items.queen, Items.queen, Items.queen,
    Items.king, Items.king, Items.king, Items.king, Items.king,
    Items.ace, Items.ace, Items.ace, Items.ace, Items.ace,
    Items.lucky888, Items.lucky888, Items.lucky888,
    Items.jackpot]

    return random.choice(symbols)

def press_to_continue():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n Press any key to continue...\"'")
    os.system('clear')
    print()

def spinning(a, b, c):
    print('\t\t------> | {} | {} | {} | <------'.format(a, b, c,t=time.sleep(.15)), end='\r')
    # reduce flicker by maxing console refresh to 60fps
    time.sleep(1/60)

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
    while(True):
        answer = input("You have $" + str(Game.credits) + ". Would you like to play? y/n ")
        answer = answer.lower().strip()
        if(answer == "y"):
            return True
        elif(answer == "n"):
            print("You ended the game with $" + str(Game.credits) + " in your hand.")
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
    want_to_play = ask_to_play()
    while(Game.credits >= 1 and want_to_play == True):
        Game.credits -= 1;
        round1 = round()
        a, b, c = round1
        print('[ {} | {} | {} ]'.format(a,b,c))
        check_win(a, b, c)
        
        if Game.credits == 0:
            print("Sorry mate, you ran out of money!")
            break;
        
        
        want_to_play = ask_to_play()

Game.credits = 20

play()