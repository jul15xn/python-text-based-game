import dialogue as dlo
from scenes.scene import Scene

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

    def 