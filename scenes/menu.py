import dialogue as dlo
import colors as cs
from scenes import cell
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
        print("(3) Quit")
        while True:
            noice = input("> ")
            if not noice.isdigit():
                cs.set_console_color(31)
                print("That is not a valid option!")
                cs.reset_colors()
            elif noice == "1":
                os.system("cls")
                cell.cell(docentmode)
                pass
            elif noice == "2":
                os.system("cls")
                cs.set_console_color(93, 101)
                print("Game Options")
                cs.reset_colors()
                print(f"\n(1) Docent mode ({docentmode})")
                op = input("> ")
                if not op.isdigit():
                    cs.set_console_color(31)
                    print("That is not a valid option!")
                    cs.reset_colors()
                elif op == "1":
                    #option mode
                    cs.set_console_color(32)
                    docentmode = not docentmode
                    print("Set option!")
                    cs.reset_colors()
                    time.sleep(2)
                    os.system("cls")
                    break
            elif noice == "3":
                print("Bye!")
                quit()
            