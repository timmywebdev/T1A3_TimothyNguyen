import os
import random
import time
import colorama
from classes import Game

def __init__(self):
    self.credits_inserted = 0

def __repr__(self):
    return f"Machine: credits_inserted={self.credits_inserted}, items={list(self._items.keys())}"

def spin_slot(first, second, third):
    print('\t\t| {} | {} | {} |'.format(first, second, third,t=time.sleep(.15)), end='\r')

def reel_randomiser():
    reel_list = ['JJJJJQQQQQKKKKKAAA8$']
    random_item = random.choice(reel_list)
    return

def reel_spin():
    for i in range(30):
        if i < 10:
            first = reel_randomiser()
            second = reel_randomiser()
            third = reel_randomiser()

            spin_slot(first, second, third)
        elif i < 20:
            first = first
            second = reel_randomiser()
            third = reel_randomiser()

            spin_slot(first, second, third)
        else:
            first = first
            second = second
            third = reel_randomiser()

            spin_slot(first, second, third)

    return (first, second, third)


def check_win(a, b, c):
    if a == "$" and b == "$" and c == "$":
        Game.winnings = 1000*Game.current_bet
        print(" *DING DING DING* JACKPOT!!!")
    elif a == "8" and b == "8" and c == "8":
        Game.winnings = 888*Game.current_bet
        print(" That is the Lucky888!")
    elif a == "A" and b == "A" and c == "A":
        Game.winnings = 50*Game.current_bet
        print(" You are an Ace")
    elif a == "K" and b == "K" and c == "K":
        Game.winnings = 20*Game.current_bet
        print(" Eat and drink like a King!")
    elif a == "Q" and b == "Q" and c == "Q":
        Game.winnings = 10*Game.current_bet
        print("*YAAAS QUEEN!")
    elif a == "J" and b == "J" and c == "J":
        Game.winnings = 5*Game.current_bet
        print(" Jack of all trades!")
    else:
        Game.winnings = 0

    if Game.winnings > 0:
        credits += Game.winnings
        print("Congratulations! You just won $" + str(Game.winnings) + "!!!")
    else:
        print("Sorry, no win this time.")
        


def play():
    os.system("clear")
    spinning()
    

def spinning():
    while(Game.credits >= 1):
        Game.credits -= Game.current_bet;
        reel_spin1 = reel_spin()
        a, b, c = reel_spin1
        layout()
        print('\t\t| {} | {} | {} |'.format(a,b,c))
        check_win(a, b, c)
        
        if Game.credits == 0:
            print("Sorry mate, you ran out of money!")
            break;


def play_game():
    use_termios = False
    try: import msvcrt
    except ImportError:
        import termios
        use_termios = True
    RUNNING = True
   
    Game()

    def flush_input():
        if use_termios:
            termios.tcflush(os.sys.stdin, termios.TCIOFLUSH)
        else:
            while msvcrt.kbhit():
                msvcrt.getch()

    def layout():
        os.system('clear')
        a = "$"
        b = "$" 
        c = "$"
        print("\t\t      Lucky Lion Slot Machine!")
        print("\t\t-----------------------------------")
        print("\t\t|     |   Winnings   |    Name    |")
        print("\t\t| $$$ |    1000x     |    Jackpot |")
        print("\t\t| 888 |     888x     |   Lucky888 |")
        print("\t\t| AAA |      50x     |       Aces |")
        print("\t\t| KKK |      20x     |      Kings |")
        print("\t\t| QQQ |      10x     |     Queens |")
        print("\t\t| JJJ |       5x     |      Jacks |")
        print("\t\t-----------------------------------")
        print("\t\t\t  -------------")
        print("\t\t    ---> ", "| {} | {} | {} |".format(a,b,c), "<---")
        print("\t\t\t  -------------\n-------------------")
        print(f" Winnings: {Game.winnings}")
        print(f" Bet Amount: {Game.current_bet}")
        print(f"\n Credits: {Game.credits}")
        print("-------------------")
        if Game.spinning: print(f"\t\t Spinning...")
        elif Game.result_message: print(f"{Game.result_message}\n")

    
    while RUNNING:
    # Initialise
        Game.game_over = False
        Game.spinning = False
        Game.current_bet = 0
        Game.result_message = ""
        Game.credits = 1000
        Game.current_prompt = 0
        Game.winnings = 0

    

        while True:
            layout()

            # If player is able to put in an input
            if Game.input_active:
                prompts = [
                    " Place a bet and press 'Enter' to spin the slots!\n (You can also put in 'Q' at any time to quit)\n > ",
                    f" Press 'Enter' to spin again or place a different bet below\n >",
                    " You should know, the house always wins...\n Game Over - You lose...Play again?(Y/N)\n >",
                    " Wow! You beat the house! Now, the house will beat you...in a dark alley.\n Game Over - You win...Play again?(Y/N)\n >"
                    " There are no credits in the machine. \n How much would you like to deposit?\n > "
                ]
                # List of error messages
                error_messages = [
                    f"  ",
                    f" Invalid input. Try again.",
                    f" Bet must be a number between 1 and {Game.credits}. Try again.",
                    f" Not enough money left!"
                ]

                error_message = 0
                while True:
                    flush_input()
                    layout()
                    # If error message is nothing, then print nothing and continue
                    if error_message != 0:
                        print(error_messages[error_message])
                        error_message = 0
                        time.sleep(2)
                        continue
                    prompt_input = input(prompts[Game.current_prompt])
                    if Game.game_over:
                        if prompt_input in ["y","Y","yes","YES","Yes"]:
                            break
                        elif prompt_input in ["n","N","no","NO","No"]:
                            RUNNING = False
                            break
                        else:
                            error_message = 1
                            continue
                    else:
                        # If user enters a number
                        if prompt_input.isdigit():
                            if Game.credits <= 0:
                                prompt_input = int(prompt_input)
                                Game.current_prompt = 4
                                prompt_input += Game.credits
                                continue
                            elif int(prompt_input) > Game.credits or int(prompt_input) < 1:
                                error_message = 2
                                continue
                            elif int(prompt_input) > Game.credits:
                                error_message = 3
                                continue
                            else:
                                credits_inserted = Game.current_bet = int(prompt_input)
                                Game.current_prompt = 1
                                break
                        elif prompt_input == "" and Game.current_prompt == 1:
                            if Game.credits < Game.current_bet:
                                error_message = 3
                                continue
                            credits_inserted = Game.current_bet
                            break
                        elif prompt_input.lower() == "q":
                            RUNNING = False
                            break
                        else:
                            err_msg = 1
                            continue
            
            if not RUNNING or Game.game_over:
                break

        Game.winnings += Game.current_bet
        Game.credits -= Game.current_bet

        Machine.play()
        spin_slot()
        check_win()

        # Check current money
        if Game.money_player <= 0:
            Game.game_over = True
            Game.current_prompt = 2

        # Cleanup
        credits_inserted = 10000
        Game.result_message = ""
        time.sleep(1)
        flush_input()

 
play_game()


Game.current_bet = 0
Game.credits = 10000
Game.winnings = 0