from scenes import menu
import colors as cs
import os

# Maak het scherm leeg
os.system("cls")

try:
    # Start het hoofdmenu van de game.
    menu.menu()
except KeyboardInterrupt:  # Afhandeling van een 'Ctrl+C' door de gebruiker.
    cs.reset_colors()  # Reset eventuele aangepaste consolekleuren.
    print("\n\nBye!")  # Print een afscheidsgroet.