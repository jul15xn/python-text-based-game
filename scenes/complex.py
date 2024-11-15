import dialogue as dlo
from scenes.scene import Scene
from scenes import conversation

class Complex(Scene):
    def __init__(self):
        super().__init__()

    def intro(self):
        dlo.print_text_dialogue("Je bent nu in het cellencomplex.<600> Je ziet heel veel cellen, <300>en aan het eind een bewaker.<600>", 2)
        dlo.new_line()
        dlo.print_text_dialogue("Ook zie je een opvallende man die opvallend naar je kijkt.<600>", 1.3)
        dlo.new_line()
        dlo.print_text_dialogue("Wat wil je doen?<400>", 0.5)
        dlo.new_line()

    def kijk_rond(self):
        dlo.print_text_dialogue("Je ziet heel veel cellen, <300>en bij de uitgang een bewaker.<600>", 2)
        dlo.new_line()
        dlo.print_text_dialogue("Ook zie je een opvallende man die opvallend naar je kijkt.<600>", 1.3)
        dlo.new_line()

    def bekijk_item(self, item_naam):
        if item_naam == "man":
            output = conversation.man_conv()
            if output == 69:
                self.inventory.append("2 euro")
                dlo.print_text_dialogue("Je hebt nu 2 euro!<300>", 0.5)
                dlo.new_line()
        if item_naam == "bewaker":
            output = conversation.bewaker_conv(self.inventory)
            if output == 68:
                self.completed = True