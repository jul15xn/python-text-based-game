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
        if len(user) >= 2 and user[0] == "kijk" and user[1] == "rond":
            current_scene.kijk_rond()
            current_scene.dialogue.new_line()
        elif len(user) >= 2 and user[0] == "bekijk":
            print("bekijk" + user[1])