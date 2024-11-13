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
        while True:
            doen = input(": ")
            doen = doen.split(" ")
            if doen[0] == "kijk" and doen[1] == "rond":
                self.kijk_rond()
                self.dialogue.new_line()

    def kijk_rond(self):
        self.dialogue.print_text_dialogue("In je cel heb je een kast,<200> een prullenbak,<200> en je bed.<600>", 3)