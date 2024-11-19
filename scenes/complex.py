import dialogue as dlo
from scenes.scene import Scene
from scenes import conversation

# Subklasse van Scene, die een specifiek cellencomplex voorstelt.
class Complex(Scene):
    def __init__(self):
        super().__init__()  # Roep de constructor van de basisklasse Scene aan.

    # Introductiemethode: wordt geroepen wanneer de speler deze scène betreedt.
    def intro(self):
        dlo.print_text_dialogue(
            "Je bent nu in het cellencomplex.<600> Je ziet heel veel cellen, <300>en aan het eind een bewaker.<600>", 2
        )
        dlo.new_line()
        dlo.print_text_dialogue(
            "Ook zie je een opvallende man die opvallend naar je kijkt.<600>", 1.3
        )
        dlo.new_line()
        dlo.print_text_dialogue("Wat wil je doen?<400>", 0.5)
        dlo.new_line()

    # Methode die de speler informatie geeft over de scène wanneer ze rondkijken.
    def kijk_rond(self):
        dlo.print_text_dialogue(
            "Je ziet heel veel cellen, <300>en bij de uitgang een bewaker.<600>", 2
        )
        dlo.new_line()
        dlo.print_text_dialogue(
            "Ook zie je een opvallende man die opvallend naar je kijkt.<600>", 1.3
        )
        dlo.new_line()

    # Methode waarmee de speler specifieke items of personages in de scène kan bekijken.
    # 'item_naam' is het doelwit dat de speler wil bekijken.
    def bekijk_item(self, item_naam):
        # Controleer of de speler de man wil bekijken.
        if item_naam == "man":
            output = conversation.man_conv()  # Start de conversatie met de man.
            if output == 69:  # Controleer of een specifieke waarde (bijvoorbeeld '69') is teruggegeven.
                self.inventory.append("2 euro")  # Voeg 2 euro toe aan de inventory.
                dlo.print_text_dialogue("Je hebt nu 2 euro!<300>", 0.5)
                dlo.new_line()
        
        # Controleer of de speler de bewaker wil bekijken.
        if item_naam == "bewaker":
            output = conversation.bewaker_conv(self.inventory)  # Start de conversatie met de bewaker.
            if output == 68:  # Controleer of een specifieke waarde (bijvoorbeeld '68') is teruggegeven.
                self.completed = True  # Markeer de scène als voltooid.