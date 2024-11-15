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
        cs.reset_colors()
        print("\n(1) Play")
        print("(2) Help")
        print("(3) Quit")
        while True:
            noice = input("> ")
            if not noice.isdigit():
                cs.set_console_color(31)
                print("That is not a valid option!")
                cs.reset_colors()
            elif noice == "1":
                os.system("cls")
                game.run_game()
                pass
            elif noice == "2":
                print("Je kan ervoor kiezen om")
                print("Rond te kijken")
                print("Iets te bekijken")
                print("Je inventory te openen")
            elif noice == "3":
                print("Bye!")
                quit()
            