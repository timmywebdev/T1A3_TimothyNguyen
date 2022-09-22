import os
from colorama import Fore
from game import check_win, spin_animation
from classes import Game
from screens import landing, press_to_continue, press_to_lever, layout, ending_loss, ending_win

def play():
    RUNNING = True    

    # RUNNING LOOP
    while RUNNING:
        Game.game_over = False
        Game.current_bet = 0
        Game.credits = 0
        Game.winnings = 0
        landing()
        while True:
            os.system("clear")
            layout()

            if Game.credits <= 0 and RUNNING is True:
                os.system("clear")
                layout()
                deposit = input(" There are currently no credits in the machine. \n How much would you like to deposit?\n > ")
                if deposit.isdigit():
                    deposit = int(deposit)
                    if deposit >= 1:
                        Game.credits += deposit
                    else: 
                        print(" Please enter a number larger than 0!")
                        press_to_continue()
                else:
                    print (" Please enter a real number!")
                    press_to_continue()
            # Put bet amount in and run the game
            while Game.credits >=1 and RUNNING is True:
                if Game.credits >=1:
                    os.system('clear')
                    layout()
                    bet = input(" Enter bet amount or enter 'q' to withdraw. \n > ")
                    if bet.isdigit():
                        bet = int(bet)
                        if bet <= Game.credits and bet > 0:
                            Game.current_bet = bet
                            Game.credits -= Game.current_bet
                            press_to_lever()
                            layout()
                        else:
                            print(f" You can only place a bet between {Fore.LIGHTGREEN_EX}$0{Fore.WHITE} and {Fore.LIGHTGREEN_EX}${Game.credits+1}{Fore.WHITE}!")
                            press_to_continue()
                            break
                    elif bet.lower() == "q":
                        ending_win()
                        exit()
                    else: 
                        print(" That is not a valid number...")
                        press_to_continue()
                        break
                   
                outcome = spin_animation()
                a, b, c = outcome #DEBUG change outcome to (Items.variable, Items.variable, Items.variable) where variable is the outcome you want to test, to test win messages.
                check_win(a, b, c)
                
                if Game.credits == 0:
                    ending_loss()
                    exit()

play()