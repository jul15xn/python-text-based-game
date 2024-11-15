from scenes.cell import Cell
from scenes.complex import Complex
from scenes.scene import *
import os
import time

current_scene = None

def game_loop(scene: Scene):
    while True:
        user = input(": ")
        user = user.split(" ")
        if user[0] == "inventory":
            scene.open_inventory()
        elif len(user) >= 2 and user[0] == "kijk" and user[1] == "rond":
            scene.kijk_rond()
        elif len(user) >= 3 and user[0] == "ga" and user[1] == "naar":
            scene.bekijk_item(user[2])
        else:
            dlo.print_text_dialogue("Onbekend commando!", 0.8, 31)
            cs.reset_colors()
            dlo.new_line()

        if scene.completed:
            break

def run_game():
    # Eerste scene
    current_scene:Scene = Cell()
    current_scene.intro()
    
    game_loop(current_scene)
    os.system("cls")

    old_inv = current_scene.inventory

    # Tweede scene
    current_scene:Scene = Complex()
    current_scene.inventory = old_inv
    current_scene.intro()

    game_loop(current_scene)

    os.system("cls")
    dlo.print_text_dialogue("Je hebt de game uitgespeeld!<400> Bedankt voor het spelen!", 1.5)
    dlo.new_line()
    dlo.print_text_dialogue("Dit is 1 van de 2 endings.<400> Dit is de main ending en er is nog een secret ending.", 2)
    dlo.new_line()
    time.sleep(10)
    dlo.print_text_dialogue("Druk op enter om af te sluiten.", 0.8)
    input()

def game_debug_2():

    # Tweede scene
    current_scene:Scene = Complex()
    current_scene.intro()

    game_loop(current_scene)