import dialogue as dlo
import colors as cs
from scenes import cell
import os
import time
import game

# Functie om het hoofdmenu van de game te tonen en opties te laten kiezen.
def menu():
    while True:  # Blijf het menu tonen totdat de speler kiest om te stoppen.
        # Stel de tekstkleur en achtergrondkleur in voor de welkomstboodschap.
        cs.set_console_color(93, 101)
        print("Welkom bij onze game!")  # Print een welkomstboodschap.
        dlo.new_line()  # Print een lege regel.
        cs.reset_colors()  # Reset kleuren naar standaardwaarden.

        # Toon de menu-opties.
        print("(1) Play")
        print("(2) Help")
        print("(3) Quit")
        
        while True:  # Blijf input vragen tot er een valide keuze is gemaakt.
            noice = input("> ")  # Vraag de gebruiker om een keuze.
            
            if not noice.isdigit():  # Controleer of de input geen getal is.
                # Geef een foutmelding in rode tekst.
                cs.set_console_color(31)
                print("Dat is geen valide optie!")  # Foutmelding voor ongeldige input.
                cs.reset_colors()
            elif noice == "1":  # Start de game.
                os.system("cls")  # Maak het scherm leeg (voor Windows).
                game.run_game()  # Roep de game-logica aan.
                quit()  # Stop het programma na het spel.
                break
            elif noice == "2":  # Toon helpinformatie.
                game.help_commando()  # Roep de helpfunctie van het spel aan.
            elif noice == "3":  # Stop de game.
                print("Bye!")  # Afscheidsboodschap.
                quit()  # Stop het programma.