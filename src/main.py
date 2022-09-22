import random
import time
import os
from colorama import *

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

def press_to_continue():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n Press any key to continue...\"'")
    os.system('clear')
    print()

def press_to_lever():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n Press any key to pull the lever...\"'")
    os.system('clear')
    print()

def reel_randomiser():
    symbols = [Items.jack, Items.jack, Items.jack, Items.jack, Items.jack,
    Items.queen, Items.queen, Items.queen, Items.queen, Items.queen,
    Items.king, Items.king, Items.king, Items.king, Items.king,
    Items.ace, Items.ace, Items.ace, Items.ace, Items.ace,
    Items.lucky888, Items.lucky888, Items.lucky888,
    Items.jackpot]

    return random.choice(symbols)

def spinning(a, b, c):
    print('\t\t------> | {} | {} | {} | <------'.format(a, b, c,t=time.sleep(.15)), end='\r')
    # reduce flicker by maxing console refresh to 60fps
    time.sleep(1/60)

def spin_animation():
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


def check_win(a, b, c):
    if a == Items.jackpot and b == Items.jackpot and c == Items.jackpot:
        Game.winnings = Items.jackpot_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTCYAN_EX}{Items.jackpot_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTCYAN_EX} *DING DING DING* JACKPOT!!!")
        press_to_continue()
    elif a == Items.lucky888 and b == Items.lucky888 and c == Items.lucky888:
        Game.winnings = Items.lucky888_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTRED_EX}{Items.lucky888_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTRED_EX} That is the Lucky888 bonus!")
        press_to_continue()
    elif a == Items.ace and b == Items.ace and c == Items.ace:
        Game.winnings = Items.ace_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTGREEN_EX}{Items.ace_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTGREEN_EX} You are an Ace")
        press_to_continue()
    elif a == Items.king and b == Items.king and c == Items.king:
        Game.winnings = Items.king_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTYELLOW_EX}{Items.king_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTYELLOW_EX} Eat and drink like a King!")
        press_to_continue()
    elif a == Items.queen and b ==Items.queen and c == Items.queen:
        Game.winnings = Items.queen_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTMAGENTA_EX}{Items.queen_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTMAGENTA_EX} *YAAAS QUEEN!")
        press_to_continue()
    elif a == Items.jack and b == Items.jack and c == Items.jack:
        Game.winnings = Items.jack_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTBLUE_EX}{Items.jack_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTBLUE_EX} Jack of all trades!")
        press_to_continue()
    else:
        print("\n\n Sorry, no win this time buddy.")
        Game.winnings = 0
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

            # Put bet amount in and run the game
            while Game.credits >=1 and RUNNING is True:

                if Game.credits >=1:
                    os.system('clear')
                    landing()
                    bet = input(" Enter bet amount or enter 'q' to withdraw. \n > ")
                    if bet.isdigit():
                        bet = int(bet)
                        if bet <= Game.credits and bet >= 0:
                            Game.current_bet = bet
                            Game.credits -= Game.current_bet
                            press_to_continue()
                            landing()
                        else:
                            print(f" You must place a bet between 0 and {Game.credits+1}!")
                            press_to_continue()
                            break
                    elif bet.lower() == "q":
                        print(f" You have left the game with ${Game.credits}! Congratulations!")
                        exit()
                    else: 
                        print(" That is not a valid number...")
                        press_to_continue()
                        break

                outcome = spin_anim()
                a, b, c = outcome
                # Check_win doesn't work either when it wins
                check_win(a, b, c)
                
                # This code below doesnt work (i think it fks up because of line 37)
                if Game.credits == 0:
                    print("Sorry mate, you ran out of money!")
                    exit()

play()