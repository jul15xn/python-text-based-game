from scenes.cell import Cell
from scenes.scene import *

current_scene = None

def run_game():
    # Eerste scene
    current_scene:Scene = Cell()
    current_scene.intro()
    while True:
        user = input(": ")
        user = user.split(" ")
        if user[0] == "inventory":
            current_scene.open_inventory()
        elif len(user) >= 2 and user[0] == "kijk" and user[1] == "rond":
            current_scene.kijk_rond()
        elif len(user) >= 2 and user[0] == "bekijk":
            current_scene.bekijk_item(user[1])