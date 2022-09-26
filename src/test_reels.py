import random
from game import Game, Items, spin_animation, reel_randomiser, check_win

# Test to see that the variables from reel_randomiser() are taken from Items.List list
def test_reel_randomiser():
    assert reel_randomiser() in Items.List

# Test to see that when you win, the Game.winnings is more than 0. If you lost, Game.winnings is equal to 0
def test_check_win():
    Game.current_bet = random.randint(1, 10000)
    outcome = spin_animation()
    a, b, c = outcome
    check_win(a, b, c)
    if Game.win == True: 
        assert Game.winnings > 0
    else: 
        assert Game.winnings == 0