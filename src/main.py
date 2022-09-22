import random
import time
import os
from colorama import *

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

def play():
    RUNNING = True    

    def landing():
        print(f"\t\t {Fore.LIGHTGREEN_EX}$$$ {Fore.LIGHTRED_EX}Lucky {Fore.LIGHTMAGENTA_EX}Lion {Fore.LIGHTRED_EX}Slot {Fore.LIGHTMAGENTA_EX}Machine {Fore.LIGHTGREEN_EX}$$$ \n")
        print(" -----------------------------------\t-------------------")
        print(f" |     |   Winnings   |    Name    |\t  Winnings: {Fore.LIGHTGREEN_EX}{Game.winnings}")
        print(f"{Fore.CYAN} | $$$ |    1000x     |    Jackpot |\t  {Fore.WHITE}Bet Amount: {Fore.LIGHTGREEN_EX}{Game.current_bet}")
        print(f"{Fore.LIGHTRED_EX} | 888 |     888x     |   Lucky888 |")
        print(f"{Fore.LIGHTGREEN_EX} | AAA |      50x     |       Aces |\t  {Fore.WHITE}Credits: {Fore.LIGHTGREEN_EX}{Game.credits}")
        print(f"{Fore.LIGHTYELLOW_EX} | KKK |      20x     |      Kings |\t{Fore.WHITE}-------------------")
        print(f"{Fore.LIGHTMAGENTA_EX} | QQQ |      10x     |     Queens |")
        print(f"{Fore.LIGHTBLUE_EX} | JJJ |       5x     |      Jacks |")
        print(" -----------------------------------")

        # reduce console flicker by limiting to 60fps
        time.sleep(1/60)

        # RUNNING LOOP
    while RUNNING:
        Game.game_over = False
        Game.current_bet = 0
        Game.credits = 0
        Game.winnings = 0

        while True:
            os.system("clear")
            landing()

            if Game.credits <= 0 and RUNNING is True:
                print("\tWelcome to the Lucky Lion Slot Machine!\n Match 3 of the same symbols to win a multiplier of your bet!")
                press_to_continue()
                landing()
                deposit = input(" There are currently no more credits in the machine. \n How much would you like to deposit?\n > ")
                if deposit.isdigit():
                    deposit = int(deposit)
                    if deposit >= 1:
                        Game.credits += deposit
                        continue
                    else: 
                        print(" Please enter a number larger than 0!")
                        break
                else:
                    print (" Please enter a real number!")
                    break

play()