import dialogue as dlo
import colors as cs
from scenes import cell
import os
import time
import game

def menu():
    docentmode = False
    while True:
        cs.set_console_color(93, 101)
        print("Welkom bij onze game!")
        dlo.new_line()
        cs.reset_colors()
        print("(1) Play")
        print("(2) Help")
        print("(3) Quit")
        while True:
            noice = input("> ")
            if not noice.isdigit():
                cs.set_console_color(31)
                print("Dat is geen valide optie!")
                cs.reset_colors()
            elif noice == "1":
                os.system("cls")
                game.run_game()
                quit()
                break
            elif noice == "2":
                game.help_commando()
            elif noice == "3":
                print("Bye!")
                quit()
            