import random
import time
from classes import *
from screens import *
from art import *
from colorama import Fore

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
        print(f"{Fore.LIGHTCYAN_EX} *DING DING DING* JACKPOT!!!{Fore.WHITE}")
        press_to_continue()
    elif a == Items.lucky888 and b == Items.lucky888 and c == Items.lucky888:
        Game.winnings = Items.lucky888_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTRED_EX}{Items.lucky888_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTRED_EX} That is the Lucky888 bonus!{Fore.WHITE}")
        press_to_continue()
    elif a == Items.ace and b == Items.ace and c == Items.ace:
        Game.winnings = Items.ace_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTGREEN_EX}{Items.ace_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTGREEN_EX} You are an Ace{Fore.WHITE}")
        press_to_continue()
    elif a == Items.king and b == Items.king and c == Items.king:
        Game.winnings = Items.king_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTYELLOW_EX}{Items.king_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTYELLOW_EX} Eat and drink like a King!{Fore.WHITE}")
        press_to_continue()
    elif a == Items.queen and b ==Items.queen and c == Items.queen:
        Game.winnings = Items.queen_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTMAGENTA_EX}{Items.queen_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTMAGENTA_EX} *YAAAS QUEEN!{Fore.WHITE}")
        press_to_continue()
    elif a == Items.jack and b == Items.jack and c == Items.jack:
        Game.winnings = Items.jack_value*Game.current_bet
        Game.credits += Game.winnings
        print(f"\n\n Congratulations! You just won {Fore.LIGHTGREEN_EX}${Game.winnings}{Fore.WHITE}!")
        print(f" This was {Fore.LIGHTBLUE_EX}{Items.jack_value}x{Fore.WHITE} your bet amount of {Fore.LIGHTGREEN_EX}${Game.current_bet}{Fore.WHITE}\n")
        print(f"{Fore.LIGHTBLUE_EX} Jack of all trades!{Fore.WHITE}")
        press_to_continue()
    else:
        print("\n\n Sorry, no win this time buddy.")
        Game.winnings = 0
        press_to_continue()