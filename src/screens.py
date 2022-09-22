import os
from classes import *
from art import text2art
from colorama import Fore

def landing():
    title1 = text2art("Lucky      Lion", font="tarty1")
    title2 = text2art("                  Slots", font = "tarty1")
    os.system("clear")
    print(f"{Fore.LIGHTGREEN_EX}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"{Fore.LIGHTRED_EX}{title1}")
    print(f"{Fore.LIGHTMAGENTA_EX}{title2}")
    print(f"{Fore.LIGHTGREEN_EX}\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    press_to_continue()

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
    print(f"{Fore.LIGHTRED_EX}{layout_title}{Fore.WHITE}")
    print(" -----------------------------------\t--------------------")
    print(f" |     |   Winnings   |    Name    |\t  Winnings: {Fore.LIGHTGREEN_EX}${Game.winnings}")
    print(f"{Fore.CYAN} | $$$ |   10000x     |    Jackpot |\t  {Fore.WHITE}Bet Amount: {Fore.LIGHTGREEN_EX}${Game.current_bet}")
    print(f"{Fore.LIGHTRED_EX} | 888 |    8888x     |   Lucky888 |")
    print(f"{Fore.LIGHTGREEN_EX} | AAA |     200x     |       Aces |\t  {Fore.WHITE}Credits: {Fore.LIGHTGREEN_EX}${Game.credits}")
    print(f"{Fore.LIGHTYELLOW_EX} | KKK |     100x     |      Kings |\t{Fore.WHITE}--------------------")
    print(f"{Fore.LIGHTMAGENTA_EX} | QQQ |      75x     |     Queens |\t{Fore.WHITE}  Match 3 to win!")
    print(f"{Fore.LIGHTBLUE_EX} | JJJ |      50x     |      Jacks |\t{Fore.WHITE} Gamble Responsibly")
    print(" -----------------------------------\t--------------------\n")

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
    print(f"{Fore.LIGHTMAGENTA_EX}{ending2}{Fore.WHITE}\n")

def ending_win():
    os.system("clear")
    ending1 = text2art(" Enjoy your", font = "tarty2")
    ending2 = text2art("  Winnings", font = "tarty2")
    print(f"{Fore.LIGHTRED_EX}{ending1}")
    print(f"{Fore.LIGHTGREEN_EX}⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⡇⠀⠀\n⣿⠀⠀⣤⣤⣤⣤⣤⣤⡄⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣷⠀⠀⠀⠀⣶⣶⣶⣶⠀⠀⣿\n⣿⠀⠀⠛⠛⣿⣿⡏⠉⠁⢀⣼⣿⣿⣿⣿⣾⣆⣤⣤⣶⣶⣶⡀⠀⢘⣿⣿⡆⠀⠀⠀⠀⠀⢹⣿⣿⠀⠀⣿⠀\n⣿⠀⠀⠀⠀⢸⣿⡇⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢰⣿⣿⠁⠀⠀⠀⠀⠀⠀⢿⣿⡇⠀⢸⡇\n⣿⠀⠀⠀⠀⢸⣿⡇⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣿⠀⠀⣿\n⣿⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⠀⠀⣿\n⣿⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠘⡿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠘⣿⣿⣦⣀⡀⠀⠀⣀⣴⣿⡿⠃⠀⠀⣿\n⣿⠀⠀⠸⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⣿\n⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⡇⠀⠀\n⠈⢹⣇⣿⡁⠀⠀⠀⠀⠀⣠⡶⢋⣡⣒⢉⣩⣬⠟⣯⣷⠭⢽⣿⢿⡫⣿⣿⣿⣟⠛⢶⡄⠀⠀⠀⠸⢧⢸⡇⠀\n⠀⠈⣧⣿⡇⠀⠀⠀⣰⠞⡋⣤⣾⣣⣶⣻⡽⠒⣿⣿⣿⣿⣦⣹⣁⣀⣿⣿⠷⠿⣷⡾⠃⠀⠀⠀⠀⣾⢸⡅⠀\n⠀⠀⢸⣿⣷⡀⠀⣸⣏⠺⣿⣿⣯⣣⡥⡴⠿⢷⣾⣿⣿⣯⣷⣿⣬⣼⣧⢴⣖⣻⣽⠇⠀⠀⠀⠀⠀⡽⢸⡇⠀\n⠀⠀⠘⠿⣍⠙⢮⡟⠀⠈⢙⣛⠟⠉⢓⠺⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⡯⢿⡿⢿⣟⣤⣤⡤⠤⣶⣿⠷⠟⠀⠀\n⠀⠀⠀⠀⠈⠛⢶⣿⣶⣾⣿⣿⣷⣶⣶⣶⣾⣶⣶⣶⣶⣿⣿⣯⣭⣷⣷⣾⣿⣿⣿⡶⠛⠛⠋⠁⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀")
    print(f"{Fore.LIGHTMAGENTA_EX}{ending2}{Fore.WHITE}\n")
    print(f" You have left the game with {Fore.LIGHTGREEN_EX}${Game.credits}{Fore.WHITE}!\n")