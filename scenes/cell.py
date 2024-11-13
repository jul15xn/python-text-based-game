import time
from scenes.scene import Scene

class Cell(Scene):
    def __init__(self):
        super().__init__()

    def intro(self):
        self.dialogue.print_text_dialogue("Je bent in een cel in de gevangenis.<600>", 2)
        self.dialogue.new_line()
        self.dialogue.print_text_dialogue("Hier ben je beland door het proberen te bestelen van de juwelier.<600>", 3)
        self.dialogue.new_line()
        self.dialogue.print_text_dialogue("Nu wil je proberen te ontsnappen uit de gevangenis.<600>", 2)
        self.dialogue.new_line()
        self.dialogue.print_text_dialogue("In je cel heb je een kast,<200> een prullenbak,<200> en je bed.<1600>", 3)
        self.dialogue.new_line()
        self.dialogue.print_text_dialogue("Wat wil je nu gaan doen?<500>", 1)
        self.dialogue.new_line()

    def kijk_rond(self):
        self.dialogue.print_text_dialogue("In je cel heb je een kast,<200> een prullenbak,<200> en je bed.<600>", 3)

    def bekijk_item(self, item_naam):
        if item_naam == "kast":
            if "kast" in self.looted:
                self.dialogue.print_text_dialogue("Dit is een kast.", 0.5)
                self.dialogue.new_line()
                return
            self.dialogue.print_text_dialogue("In de kast zit een zakje coke. Wil je deze meenemen?", 2)
            self.dialogue.new_line()
            meeneem = input(": ").lower()
            if meeneem == "ja":
                self.looted.append("kast")
                self.inventory.append("coke")
                self.dialogue.print_text_dialogue("Je hebt nu de coke.", 0.8)
                self.dialogue.new_line()
        if item_naam == "prullenbak":
            if "prullenbak" in self.looted:
                self.dialogue.print_text_dialogue("Dit is een prullenbak.", 0.6)
                self.dialogue.new_line()
                return
            self.dialogue.print_text_dialogue("In de prullenbak zit een hamer. Wil je deze meenemen?", 2)
            self.dialogue.new_line()
            meeneem = input(": ").lower()
            if meeneem == "ja":
                self.looted.append("prullenbak")
                self.inventory.append("hamer")
                self.dialogue.print_text_dialogue("Je hebt nu de hamer.", 0.8)
                self.dialogue.new_line()