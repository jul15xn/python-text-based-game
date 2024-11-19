import dialogue as dlo
import colors as cs

# Basisklasse voor een scène in het spel.
class Scene:
    inventory = []  # Een lijst van items die de speler heeft verzameld.
    looted = []  # Een lijst van items die al zijn gebruikt in de scène.

    def __init__(self):
        # Geeft aan of de scène is voltooid. Standaard is dit False.
        self.completed = False

    # Introductie van de scène. Kan worden overschreven door subclasses.
    def intro(self):
        pass

    # Methode om rond te kijken in de scène. Kan worden overschreven door subclasses.
    def kijk_rond(self):
        pass

    # Methode om een specifiek item te bekijken in de scène.
    # 'item_naam' is de naam van het item dat de speler wil bekijken.
    def bekijk_item(self, item_naam):
        pass

    # Methode om de inventory te openen en de inhoud ervan te tonen.
    def open_inventory(self):
        # Controleer of de inventory leeg is.
        if len(self.inventory) < 1:
            dlo.print_text_dialogue("Je hebt niks in je inventory!", 1.2)  # Print een melding.
            dlo.new_line()  # Voeg een lege regel toe.
            return
        
        # Als de inventory niet leeg is, toon alle items.
        dlo.print_text_dialogue("Dit zit er in je inventory:", 1.5)
        dlo.new_line()

        for item in self.inventory:  # Loop door elk item in de inventory.
            dlo.print_text_dialogue(f"- {item}", 0.5)  # Print elk item met een kleine vertraging.
            dlo.new_line()