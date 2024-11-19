# BELANGRIJK!!!!!!!!!!!!!!!!!!!!!!!
# In het kleuren.png bestand staan de kleuren die je kan gebruiken.
# Alleen de nummers voor foreground kan je voor de tekstkleur gebruiken
# en alleen de nummers voor de background is voor de achtergrondkleur.

# Functie om een tekstkleur en achtergrondkleur toe te passen door middel van ANSI escape codes.
# De standaardkleur voor tekst is wit (37) en de standaardkleur voor de achtergrond is zwart (40).
def set_color(text, foreground = 37, background = 40):
    return f"[{background};{foreground}m{text}"  # Format de tekst met kleurinstellingen.

# Functie om de consolekleur aan te passen zonder de tekst te wijzigen.
# De standaardkleur voor de tekst is wit (37) en voor de achtergrond zwart (40).
def set_console_color(foreground = 37, background = 40):
    print(f"[{background};{foreground}m", end='')  # Zet de kleur voor de console-output zonder tekst te printen.

# Functie om de kleuren van de console weer naar de standaardinstelling te herstellen.
def reset_colors():
    print(f"[0m", end='')  # Herstelt de kleuren naar de standaardinstelling (geen kleur).
