import dialogue as dlo
from scenes.scene import Scene

class Complex(Scene):
    def __init__(self):
        super().__init__()

    def intro(self):
        dlo.print_text_dialogue("")