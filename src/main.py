from colorama import Fore
import os
import random

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

def layout():
    # print(f"{Fore.LIGHTRED_EX}{layout_title}")
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
    return random.choice('JJJJJQQQQQKKKKKAAAAA88$')

while RUNTIME:
    # Initialize
    Game.game_over = False
    Game.spinning = False
    Game.current_bet = 0
    Game.current_result = ""
    Game.money_player = 10000

    # Setup slot machine
    SlotMachine().item_add("Jackpot",[300,600,1000],"$",colorama.Fore.LIGHTCYAN_EX)
    SlotMachine().item_add("Lucky888",[100,200,300],"8",colorama.Fore.LIGHTRED_EX)
    SlotMachine().item_add("Aces",[50,100,150],"A",colorama.Fore.LIGHTGREEN_EX)
    SlotMachine().item_add("Kings",[20,40,60],"K",colorama.Fore.LIGHTYELLOW_EX)
    SlotMachine().item_add("Queens",[10,20,30],"Q",colorama.Fore.LIGHTMAGENTA_EX)
    SlotMachine().item_add("Jacks",[5,10,15],"J",colorama.Fore.LIGHTBLUE_EX)
    SlotMachine().item_add(" ",[0,0,0],"-")
    SlotMachine().reel_setup(0,["Jackpot", " ", "Kings", " ", "Lucky888", " ", "Queens", " ", "Aces", " ", "Jacks", " "])
    SlotMachine().reel_setup(1,["Lucky888", " ", "Queens", " ", "Jacks", " ", "Aces", " ", "Kings", " ", "Jackpot", " "])
    SlotMachine().reel_setup(2,["Aces", " ", "Jacks", " ", "Lucky888", " ", "Queens", " ", "Jackpot", " ", "Kings", " "])

    slot_probability = {
        "Jackpot":random.randint(1,15),
        "Lucky888":random.randint(1,20),
        "Aces":random.randint(1,25),
        "Kings":random.randint(1,40),
        "Queens":random.randint(1,50),
        "Jacks":random.randint(1,70),
    }