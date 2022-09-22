import random
import time
import os
import colorama
from colorama import Fore

class Game:
    current_bet = 0
    winnings = 0
    credits = 0

def reel_randomiser():
    symbols = [ Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE , Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE , Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE , Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE , Fore.LIGHTBLUE_EX + 'J' + Fore.WHITE , 
    Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, Fore.LIGHTMAGENTA_EX + 'Q' + Fore.WHITE, 
    Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, Fore.LIGHTYELLOW_EX + 'K' + Fore.WHITE, 
    Fore.LIGHTGREEN_EX + 'A' + Fore.WHITE, Fore.LIGHTGREEN_EX + 'A' + Fore.WHITE, Fore.LIGHTGREEN_EX + 'A' + Fore.WHITE, 
    Fore.LIGHTRED_EX + '8' + Fore.WHITE, Fore.LIGHTRED_EX + '8' + Fore.WHITE, 
    Fore.LIGHTCYAN_EX + '$' + Fore.WHITE]

    return random.choice(symbols)

def spinning(a, b, c):
    print('\t\t   ------> | {} | {} | {} | <------'.format(a, b, c,t=time.sleep(.15)), end='\r')