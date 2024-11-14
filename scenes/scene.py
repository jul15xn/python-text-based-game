import dialogue as dlo
import colors as cs

class Scene:
    inventory = []
    looted = []

    def __init__(self):
        self.completed = False

    def intro(self):
        pass

    def kijk_rond(self):
        pass

    def bekijk_item(self, item_naam):
        pass

    def open_inventory(self):
        if len(self.inventory) < 1:
            dlo.print_text_dialogue("Je hebt niks in je inventory!", 1.2)
            dlo.new_line()
            return
        
        dlo.print_text_dialogue("Dit zit er in je inventory:", 1.5)
        dlo.new_line()

        for item in self.inventory:
            dlo.print_text_dialogue(f"- {item}", 0.5)
            dlo.new_line()