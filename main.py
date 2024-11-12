from scenes import menu
import colors as cs
import os

os.system("cls")
try:
    menu.menu()
except KeyboardInterrupt:
    cs.reset_colors()
    print("\n\nBye!")