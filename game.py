from scenes.cell import Cell
from scenes.complex import Complex
from scenes.scene import *
import os

current_scene = None

def game_loop():
    while True:
        user = input(": ")
        user = user.split(" ")
        if user[0] == "inventory":
            current_scene.open_inventory()
        elif len(user) >= 2 and user[0] == "kijk" and user[1] == "rond":
            current_scene.kijk_rond()
        elif len(user) >= 2 and user[0] == "bekijk":
            current_scene.bekijk_item(user[1])

        if current_scene.completed:
            break

def run_game():
    # Eerste scene
    current_scene:Scene = Cell()
    current_scene.intro()
    
    game_loop()
    os.system("cls")

    # Tweede scene
    current_scene:Scene = Complex()
    current_scene.intro()

    game_loop()