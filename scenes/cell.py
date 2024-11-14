import time
from scenes.scene import Scene
import dialogue as dlo

class Cell(Scene):
    def __init__(self):
        super().__init__()

    def intro(self):
        dlo.print_text_dialogue("Je bent in een cel in de gevangenis.<600>", 2)
        dlo.new_line()
        dlo.print_text_dialogue("Hier ben je beland door het proberen te bestelen van de juwelier.<600>", 3)
        dlo.new_line()
        dlo.print_text_dialogue("Nu wil je proberen te ontsnappen uit de gevangenis.<600>", 2)
        dlo.new_line()
        self.kijk_rond()
        dlo.print_text_dialogue("Wat wil je nu gaan doen?<500>", 1)
        dlo.new_line()

    def kijk_rond(self):
        dlo.print_text_dialogue("In je cel heb je een kast,<200> een prullenbak,<200> en je bed.<300>", 3)
        dlo.new_line()
        dlo.print_text_dialogue("Ook zit er een klein gat boven je bed.<300> Je kan er net doorheen kijken en ziet een hele doorgang erin.<600>", 3.5)
        dlo.new_line()

    def bekijk_item(self, item_naam):
        if item_naam == "kast":
            if "kast" in self.looted:
                dlo.print_text_dialogue("Dit is een kast.", 0.5)
                dlo.new_line()
                return
            dlo.print_text_dialogue("In de kast zit een zakje coke. Wil je deze meenemen?", 2)
            dlo.new_line()
            meeneem = input(": ").lower()
            if meeneem == "ja":
                self.looted.append("kast")
                self.inventory.append("coke")
                dlo.print_text_dialogue("Je hebt nu de coke.", 0.8)
                dlo.new_line()
        if item_naam == "prullenbak":
            if "prullenbak" in self.looted:
                dlo.print_text_dialogue("Dit is een prullenbak.", 0.6)
                dlo.new_line()
                return
            dlo.print_text_dialogue("In de prullenbak zit een hamer. Wil je deze meenemen?", 2)
            dlo.new_line()
            meeneem = input(": ").lower()
            if meeneem == "ja":
                self.looted.append("prullenbak")
                self.inventory.append("hamer")
                dlo.print_text_dialogue("Je hebt nu de hamer.", 0.8)
                dlo.new_line()
        if item_naam == "gat":
            dlo.print_text_dialogue()
