from dialogue import *
import colors as cs
import game
import os
import time


def menu():
    docentmode = False
    while True:
        cs.set_console_color(93, 101)
        print("Welkom bij onze game!")
        cs.reset_colors()
        print("\n(1) Play")
        print("(2) Options")
        print("(3) Help")
        print("(4) Quit")
        while True:
            noice = input("> ")
            if not noice.isdigit():
                cs.set_console_color(31)
                print("That is not a valid option!")
                cs.reset_colors()
            elif noice == "1":
                os.system("cls")
                game.run_game()
                continue
            elif noice == "2":
                os.system("cls")
                cs.set_console_color(93, 101)
                print("Game Options")
                cs.reset_colors()
                print(f"\n(1) Docent mode ({docentmode})")
                global DIALOGUE_DEBUG
                print(f"(2) Debug mode ({DIALOGUE_DEBUG})")
                op = input("> ")
                if not op.isdigit():
                    cs.set_console_color(31)
                    print("That is not a valid option!")
                    cs.reset_colors()
                elif op == "1":
                    #option mode
                    cs.set_console_color(32)
                    docentmode = not docentmode
                    print(f"Set docent mode to {docentmode}!")
                    cs.reset_colors()
                    time.sleep(2)
                    os.system("cls")
                    break
                elif op == "2":
                    #option mode
                    cs.set_console_color(32)
                    DIALOGUE_DEBUG = not DIALOGUE_DEBUG
                    print(f"Set debug mode to {DIALOGUE_DEBUG}!")
                    cs.reset_colors()
                    time.sleep(2)
                    os.system("cls")
                    break
            elif noice == "3":
                print("DOE HIER DE HELP KANKER DANI")
            elif noice == "4":
                print("Bye!")
                quit()
            