# This exec function is used to execute the program by helping the user install dependencies
from pip_exec import pip_exec
pip_exec()

import os
from colorama import Fore
# from pip_exec import pip_exec
from game import check_win, spin_animation, Game
from screens import landing, layout, ending_loss, ending_win
from newpage import press_to_continue, flush_input, press_to_lever


def play():
    RUNNING = True    

    # RUNNING LOOP
    while RUNNING:
        Game.game_over = False
        Game.current_bet = 0
        Game.credits = 0
        Game.winnings = 0
        Game.win = False
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
                flush_input()
                os.system('clear')
                layout()
                bet = input(" Enter bet amount or enter 'q' to withdraw. \n If you have made a previous bet, press 'Enter' to repeat your bet. \n > ")
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

                elif Game.current_bet > 0 and bet == "":
                    bet = Game.current_bet
                    Game.credits -= Game.current_bet
                    press_to_lever()
                    layout()              
                elif bet.lower() == "q":
                    ending_win()
                    exit()
                else: 
                    print(" That is not a valid number...")
                    flush_input()
                    press_to_continue()
                    break
                   
                outcome = spin_animation()
                a, b, c = outcome #DEBUG change outcome to (Items.variable, Items.variable, Items.variable) where variable is the outcome you want to test, to test win messages.
                flush_input()
                check_win(a, b, c)
                
                if Game.credits == 0:
                    flush_input()
                    ending_loss()
                    exit()

play()