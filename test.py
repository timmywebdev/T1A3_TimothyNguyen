#deposit
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


#feature 2: bet
while Game.credits >=1 and RUNNING is True:
    if Game.credits >=1:
        flush_input()
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
            flush_input()
            press_to_continue()
            break

#feature 3: slot machine spinning
    #part 1:
def reel_randomiser():
    symbols = [Items.jack, Items.jack, Items.jack, Items.jack, Items.jack,
                Items.queen, Items.queen, Items.queen, Items.queen, Items.queen,
                Items.king, Items.king, Items.king, Items.king, Items.king,
                Items.ace, Items.ace, Items.ace, Items.ace, Items.ace,
                Items.lucky888, Items.lucky888, Items.lucky888,
                Items.jackpot]

    return random.choice(symbols)

    #part 2a (spinning animation + print):
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

    #part2b (printing the animation with formatting so it clears before next print)
def spinning(a, b, c):
    print('\t\t------> | {} | {} | {} | <------'.format(a, b, c,t=time.sleep(.15)), end='\r')
    # reduce flicker by maxing console refresh to 60fps
    time.sleep(1/60)

#feature 4: checking for the win
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
