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
    