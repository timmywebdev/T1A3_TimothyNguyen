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

while True:
    credits = 100
    print("Welcome to the Mapogo Lion Slot Machine")
    while credits > 0:
        print ("Credits: ", credits)
        try:
            bet = int(input("Bet amount: "))
        except:
            print("Please enter a whole number of credits.")
            continue
        for key, values in symbols.items():
            if bet > credits:
                print("Not enough credits.")
            else:
                credits -= bet
                L11 = random.choice(list(symbols.keys()))
                L12 = random.choice(list(symbols.keys()))
                L13 = random.choice(list(symbols.keys()))
                L14 = random.choice(list(symbols.keys()))
                L15 = random.choice(list(symbols.keys()))
                L21 = random.choice(list(symbols.keys()))
                L22 = random.choice(list(symbols.keys()))
                L23 = random.choice(list(symbols.keys()))
                L24 = random.choice(list(symbols.keys()))
                L25 = random.choice(list(symbols.keys()))
                L31 = random.choice(list(symbols.keys()))
                L32 = random.choice(list(symbols.keys()))
                L33 = random.choice(list(symbols.keys()))
                L34 = random.choice(list(symbols.keys()))
                L35 = random.choice(list(symbols.keys()))
                L41 = random.choice(list(symbols.keys()))
                L42 = random.choice(list(symbols.keys()))
                L43 = random.choice(list(symbols.keys()))
                L44 = random.choice(list(symbols.keys()))
                L45 = random.choice(list(symbols.keys()))
                L51 = random.choice(list(symbols.keys()))
                L52 = random.choice(list(symbols.keys()))
                L53 = random.choice(list(symbols.keys()))
                L54 = random.choice(list(symbols.keys()))
                L55 = random.choice(list(symbols.keys()))

                # L55 = random.choices(list(symbols.keys()), weights = symbols_prob)
            
                print()

                print("|", L11, "|", L12, "|", L13, "|", L14, "|", L15, "|")
                print("----------------------")

                print("|", L21, "|", L22, "|", L23, "|", L24, "|", L25, "|")
                print("----------------------")

                print("|", L31, "|", L32, "|", L33, "|", L34, "|", L35, "|")
                print("----------------------")

                print("|", L41, "|", L42, "|", L43, "|", L44, "|", L45, "|")
                print("----------------------")

                print("|", L51, "|", L52, "|", L53, "|", L54, "|", L55, "|")
                print()
                
                if L11 == L12 == L13 or L21 == L22 == L23 or L31 == L32 == L33 or L41 == L42 == L43 or L51 == L52 == L53:
                    amount_won = bet*(values)
                    print(values)
                    print("Amount won: ", amount_won)
                    credits += amount_won
                    break
                elif L11 == L12 == L13 == L14 or L21 == L22 == L23 == L24 or L31 == L32 == L33 == L34 or L41 == L42 == L43 == L44 or L51 == L52 == L53 == L54:
                    amount_won = bet*(values)
                    print(values)
                    print("Amount won: ", amount_won)
                    credits += amount_won
                    break
                else: 
                    print("You lose!")
                    break
    
    print("You are out of credits.")
    print("Thank you for playing.")
    print()
     
