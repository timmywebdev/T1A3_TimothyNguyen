import random
import time
import os
from art import *
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

def press_to_continue():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n Press any key to continue...\"'")
    os.system('clear')
    print()

def press_to_lever():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n Press any key to pull the lever...\"'")
    os.system('clear')
    print()

def layout():
    layout_title = text2art("    Lucky Lion Slots", font="tarty2")
    print(f"{Fore.LIGHTRED_EX}{layout_title}")
    print(" -----------------------------------\t--------------------")
    print(f" |     |   Winnings   |    Name    |\t  Winnings: {Fore.LIGHTGREEN_EX}${Game.winnings}")
    print(f"{Fore.CYAN} | $$$ |   10000x     |    Jackpot |\t  {Fore.WHITE}Bet Amount: {Fore.LIGHTGREEN_EX}${Game.current_bet}")
    print(f"{Fore.LIGHTRED_EX} | 888 |    8888x     |   Lucky888 |")
    print(f"{Fore.LIGHTGREEN_EX} | AAA |     200x     |       Aces |\t  {Fore.WHITE}Credits: {Fore.LIGHTGREEN_EX}${Game.credits}")
    print(f"{Fore.LIGHTYELLOW_EX} | KKK |     100x     |      Kings |\t{Fore.WHITE}--------------------")
    print(f"{Fore.LIGHTMAGENTA_EX} | QQQ |      75x     |     Queens |\t{Fore.WHITE}  Match 3 to win!")
    print(f"{Fore.LIGHTBLUE_EX} | JJJ |      50x     |      Jacks |\t{Fore.WHITE} Gamble Responsibly")
    print(" -----------------------------------\t--------------------\n")


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

def landing():
    title1 = text2art("Lucky      Lion", font="tarty1")
    title2 = text2art("                  Slots", font = "tarty1")
    os.system("clear")
    print(f"{Fore.LIGHTGREEN_EX}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"{Fore.LIGHTRED_EX}{title1}")
    print(f"{Fore.LIGHTMAGENTA_EX}{title2}")
    print(f"{Fore.LIGHTGREEN_EX}\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    press_to_continue()

def ending_loss():
    ending1 = text2art("Better luck", font = "tarty2")
    ending2 = text2art(" Next time!", font = "tarty2")
    print(f"{Fore.LIGHTRED_EX}{ending1}")
    print(f"{Fore.LIGHTGREEN_EX}⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠒⠒⠲⢤⣀⢀⣀⡤⠤⠦⢤⡀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⢀⣠⣤⠤⢤⣄⣈⢿⠁⠀⠀⠀⠀⠙⣦⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣠⠏⠀⠘⠋⠀⠀⢀⣀⣤⣬⣿⣿⡛⠉⣉⣭⣽⣿⣶⣤⣀⠀\n⠀⠀⠀⠀⣠⡴⠋⠀⠀⢀⡠⣶⣾⠿⠒⠋⣉⣉⣛⣻⣶⠞⣚⣻⣯⣍⣓⣾⣇\n⠀⠀⠀⡾⠁⠀⠀⠀⠀⠻⠿⣭⣤⠖⢺⣿⣻⠻⣄⢠⡟⠉⠁⣼⢭⡛⣷⢀⣹\n⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠙⠺⠿⣾⣿⣿⣿⣿⠿⢋⠉⠛⠛⠛⠛⣻⠟⠁\n⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠶⠚⠉⠀⠀⠈⠙⠶⡒⠛⠻⣅⠀⠀\n⢾⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣆⠀\n⠸⡆⠀⠀⠀⠀⠀⠀⢠⡞⠩⢭⣬⣭⣉⣙⡓⠒⠶⠶⠶⠶⠒⠒⠛⠉⣉⣽⠀\n⠀⠹⣄⠀⠀⠀⠀⠀⣆⡳⠶⠒⠒⠒⠶⠭⢭⣭⣉⣙⣛⣛⣛⡋⢉⣉⡿⠀⠀\n⠀⠀⠈⠿⣶⣤⣀⣀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣉⡭⠟⠉⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⠉⠙⠛⠻⠽⢿⣿⣖⣒⣒⣒⣒⣺⡿⠟⠉⠉⠀⠀⠀⠀⠀⠀⠀")
    print(f"{Fore.LIGHTRED_EX}{ending2}{Fore.WHITE}\n")

def ending_win():
    os.system("clear")
    ending1 = text2art(" Enjoy your", font = "tarty2")
    ending2 = text2art("  Winnings", font = "tarty2")
    print(f"{Fore.LIGHTMAGENTA_EX}{ending1}")
    print(f"{Fore.LIGHTGREEN_EX}⠀⠀⢀⣠⠤⠶⠖⠒⠒⠶⠦⠤⣄⠀⠀⠀⣀⡤⠤⠤⠤⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣦⠞⠁⠀⠀⠀⠀⠀⠀⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⡾⠁⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢀⡴⠚⠉⠁⠀⠀⠀⠀⠈⠉⠙⠲⣄⣤⠤⠶⠒⠒⠲⠦⢤⣜⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠹⣆⠀⠀⠀⠀⠀⠀⣀⣀⣀⣹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣠⠞⣉⣡⠤⠴⠿⠗⠳⠶⣬⣙⠓⢦⡈⠙⢿⡀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡿⣷⣤⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⣾⣡⠞⣁⣀⣀⣀⣠⣤⣤⣤⣄⣭⣷⣦⣽⣦⡀⢻⡄⠰⢟⣥⣾⣿⣏⣉⡙⠓⢦⣻⠃⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠉⠉⠙⠻⢤⣄⣼⣿⣽⣿⠟⠻⣿⠄⠀⠀⢻⡝⢿⡇⣠⣿⣿⣻⣿⠿⣿⡉⠓⠮⣿⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠙⢦⡈⠛⠿⣾⣿⣶⣾⡿⠀⠀⠀⢀⣳⣘⢻⣇⣿⣿⣽⣿⣶⣾⠃⣀⡴⣿⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⠤⢄⣈⣉⣙⣓⣒⣒⣚⣉⣥⠟⠀⢯⣉⡉⠉⠉⠛⢉⣉⣡⡾⠁⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⣠⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡿⠋⠀⠀⠀⠀⠈⠻⣍⠉⠀⠺⠿⠋⠙⣦⠀⠀⠀⠀⠀⠀⠀\n⠀⣀⣥⣤⠴⠆⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀\n⠸⢫⡟⠙⣛⠲⠤⣄⣀⣀⠀⠈⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⣨⠇⠀⠀⠀⠀⠀\n⠀⠀⠻⢦⣈⠓⠶⠤⣄⣉⠉⠉⠛⠒⠲⠦⠤⠤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⠴⢋⡴⠋⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠉⠓⠦⣄⡀⠈⠙⠓⠒⠶⠶⠶⠶⠤⣤⣀⣀⣀⣀⣀⣉⣉⣉⣉⣉⣀⣠⠴⠋⣿⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠒⠒⠒⠒⠒⠤⠤⠤⠒⠒⠒⠒⠒⠒⠚⢉⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠛⠳⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠚⠁⠀⠀⠀⠀⠘⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠙⢷⡋⢙⡇⢀⡴⢒⡿⢶⣄⡴⠀⠙⠳⣄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠈⠛⢻⠛⢉⡴⣋⡴⠟⠁⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠘⣶⢋⡞⠁⠀⠀⢀⡴⠂⠀⠀⠀⠀⠹⣄⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠈⠻⢦⡀⠀⣰⠏⠀⠀⢀⡴⠃⢀⡄⠙⣆")
    print(f"{Fore.LIGHTMAGENTA_EX}{ending2}{Fore.WHITE}\n")
    print(f" You have left the game with {Fore.LIGHTGREEN_EX}${Game.credits}{Fore.WHITE}!\n")
