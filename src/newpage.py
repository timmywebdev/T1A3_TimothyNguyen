import os

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def press_to_continue():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n Press any key to continue...\"'")
    os.system('clear')
    print()

def press_to_lever():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\n Press any key to pull the lever...\"'")
    os.system('clear')
    print()