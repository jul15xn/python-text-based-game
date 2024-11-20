from scenes.cell import Cell
from scenes.complex import Complex
from scenes.scene import *
import os
import time

# Variabele om de huidige scène van het spel bij te houden.
current_scene = None

# Functie die de speler laat zien welke commando's mogelijk zijn in het spel.
def help_commando():
    print("Je kan ervoor kiezen om:")  # Overzicht van commando's
    print("Rond te kijken (kijk rond)")
    print("Iets te bekijken (ga naar [item])")
    print("Je inventory te openen (inventory)")
    print("Dit help command weer te geven (help)")
    print("Alles tussen de haakjes kan je intypen in game.")

# Functie om het spel te herstarten.
def restart_game():
    os.system("cls")  # Clear de console.
    cs.set_console_color(92)
    print("Het spel wordt opnieuw gestart...")
    cs.reset_colors()
    time.sleep(2)  # Wacht 2 seconden voor de herstart.
    os.system("cls")
    run_game()  # Start het spel opnieuw.

# De hoofdgame-loop voor een specifieke scène.
def game_loop(scene: Scene):
    while True:
        user = input(": ").lower()  # Vraag de speler om input en maak het lowercase.
        user = user.split(" ")  # Splits de input op basis van spaties.
        
        # Controleer welk commando is ingevoerd.
        if user[0] == "inventory":  # Open de inventory.
            scene.open_inventory()
        elif len(user) >= 2 and user[0] == "kijk" and user[1] == "rond":  # Kijk rond in de scène.
            scene.kijk_rond()
        elif len(user) >= 3 and user[0] == "ga" and user[1] == "naar":  # Ga naar een specifiek item.
            scene.bekijk_item(user[2])
        elif user[0] == "help" and len(user) == 1:  # Toon de helpinformatie.
            help_commando()
        elif len(user) == 1 and user[0] == "restart":  # Vraag om bevestiging voor herstart.
            dlo.print_text_dialogue("Weet je zeker dat je de HELE game wilt restarten? Zo ja, typ 'restart confirm'", 2, 33)
            cs.reset_colors()
            dlo.new_line()
        elif len(user) == 2 and user[0] == "restart" and user[1] == "confirm":  # Herstart het spel.
            restart_game()
            break  # Verlaat de huidige game-loop.
        else:  # Als het commando niet wordt herkend, toon een foutmelding.
            dlo.print_text_dialogue("Onbekend commando!", 0.8, 31)  # Rood gekleurde tekst.
            cs.reset_colors()
            dlo.new_line()

        # Als de scène is voltooid, stop de loop.
        if scene.completed:
            break

# Functie om het spel te starten.
def run_game():
    # Eerste scène instellen.
    current_scene: Scene = Cell()  # Start in een cel (voorbeeld).
    current_scene.intro()  # Toon de intro van de scène.
    
    game_loop(current_scene)  # Start de game-loop voor deze scène.
    os.system("cls")  # Clear de console.

    # Sla de inventory van de eerste scène op.
    old_inv = current_scene.inventory

    # Tweede scène instellen.
    current_scene: Scene = Complex()  # Ga naar een complex (voorbeeld).
    current_scene.inventory = old_inv  # Zet de oude inventory over.
    current_scene.intro()  # Toon de intro van de tweede scène.

    game_loop(current_scene)  # Start de game-loop voor deze scène.

    os.system("cls")  # Clear de console.
    
    # Eindboodschap en credits.
    dlo.print_text_dialogue("Je hebt de game uitgespeeld!<400> Bedankt voor het spelen!", 1.5)
    dlo.new_line()
    dlo.print_text_dialogue("Dit is 1 van de 2 endings.<400> Dit is de main ending en er is nog een secret ending.", 2)
    dlo.new_line()
    time.sleep(10)  # Wacht 10 seconden.
    dlo.print_text_dialogue("Druk op enter om af te sluiten.", 0.8)
    input()  # Wacht tot de speler op Enter drukt.
