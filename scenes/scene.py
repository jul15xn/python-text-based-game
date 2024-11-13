import dialogue as dlo
import colors as cs

class Scene:
    dialogue: dlo = dlo
    colors: cs = cs
    inventory = []
    looted = []

    def __init__(self):
        pass

    def intro(self):
        pass

    def kijk_rond(self):
        pass

    def bekijk_item(self, item_naam):
        pass

    def open_inventory(self):
        if len(self.inventory) < 1:
            self.dialogue.print_text_dialogue("Je hebt niks in je inventory!", 1.2)
            self.dialogue.new_line()
            return
        x = ""
        for item in self.inventory:
            x += f"- {item}\n"
        self.dialogue.print_text_dialogue("Dit zit er in je inventory:\n" + x, 3)
        self.dialogue.new_line()