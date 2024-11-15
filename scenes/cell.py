import time
from scenes.scene import Scene
import dialogue as dlo

class Cell(Scene):
    def __init__(self):
        super().__init__()

    def intro(self):
        dlo.print_text_dialogue("Je bent in een cel in de gevangenis.<600>", 1)
        dlo.new_line()
        dlo.print_text_dialogue("Hier ben je beland door het proberen te bestelen van de juwelier.<600>", 2)
        dlo.new_line()
        dlo.print_text_dialogue("Nu wil je proberen te ontsnappen uit de gevangenis.<600>", 1)
        dlo.new_line()
        self.kijk_rond()
        dlo.print_text_dialogue("Wat wil je nu gaan doen?<500>", 1)
        dlo.new_line()

    def kijk_rond(self):
        dlo.print_text_dialogue("In je cel heb je een kast,<200> een prullenbak,<200> en je bed.<300>", 1.7)
        dlo.new_line()
        dlo.print_text_dialogue("Ook zit er een klein gat boven je bed.<600>", 1)
        dlo.new_line()

    def bekijk_item(self, item_naam):
        if item_naam == "kast":
            if "kast" in self.looted:
                dlo.print_text_dialogue("Dit is een kast.", 0.5)
                dlo.new_line()
                return
            dlo.print_text_dialogue("In de kast zit een zakje muesli. Wil je deze meenemen? (JA/NEE)", 2)
            dlo.new_line()
            meeneem = input(": ").lower()
            if meeneem == "ja":
                self.looted.append("kast")
                self.inventory.append("muesli")
                dlo.print_text_dialogue("Je hebt nu de muesli.", 0.8)
                dlo.new_line()
        if item_naam == "prullenbak":
            if "prullenbak" in self.looted:
                dlo.print_text_dialogue("Dit is een prullenbak.", 0.6)
                dlo.new_line()
                return
            dlo.print_text_dialogue("In de prullenbak zit een hamer. Wil je deze meenemen? (JA/NEE)", 2)
            dlo.new_line()
            meeneem = input(": ").lower()
            if meeneem == "ja":
                self.looted.append("prullenbak")
                self.inventory.append("hamer")
                dlo.print_text_dialogue("Je hebt nu de hamer.", 0.8)
                dlo.new_line()

        if item_naam == "bed":
            dlo.print_text_dialogue("Dit is je bed.<300> Je bed is erg groot.<500>", 1.5)
            dlo.new_line()
            self.bekijk_item("gat")
        if item_naam == "gat":
            dlo.print_text_dialogue("Er zit een klein gat boven je bed.<500> Je kan er deels doorheen kijken en je ziet een lange doorgang.<600>", 2)
            dlo.new_line()
            if "hamer" in self.inventory:
                dlo.print_text_dialogue("Je hebt een hamer bij je.<400> Wil je het gat groter maken? (JA/NEE)", 1.5)
                dlo.new_line()
                meeneem = input(": ").lower()
                if meeneem == "ja":
                    dlo.print_text_dialogue("Het gat is groot genoeg om doorheen te gaan.<600> Je ziet er een lange gang doorheen.<500>", 1.5)
                    dlo.new_line()
                    dlo.print_text_dialogue("Je gaat door de gang heen,<300> en je komt uit bij een vent.<500>", 1)
                    dlo.new_line()
                    dlo.print_text_dialogue("Je maakt deze vent open en je komt in een cellencomplex.<1500>", 1.5)
                    dlo.new_line()
                    self.completed = True
                    return
                
            else:
                dlo.print_text_dialogue("Misschien kan je dit gat groter maken met een bepaald item,<300> iets van een hamer ofzo.", 2.5)
                dlo.new_line()
                
        