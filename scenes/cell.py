import time
from scenes.scene import Scene
import dialogue as dlo

# Klasse die een specifieke cel in een gevangenis voorstelt, afgeleid van Scene.
class Cell(Scene):
    def __init__(self):
        super().__init__()  # Roep de constructor van de basisklasse Scene aan.

    # Introductiemethode: beschrijft de situatie wanneer de speler deze scène betreedt.
    def intro(self):
        dlo.print_text_dialogue("Je bent in een cel in de gevangenis.<600>", 1)
        dlo.new_line()
        dlo.print_text_dialogue("Hier ben je beland door het proberen te bestelen van de juwelier.<600>", 2)
        dlo.new_line()
        dlo.print_text_dialogue("Nu wil je proberen te ontsnappen uit de gevangenis.<600>", 1)
        dlo.new_line()
        self.kijk_rond()  # Geef de speler een overzicht van de omgeving.
        dlo.print_text_dialogue("Wat wil je nu gaan doen?<500>", 1)
        dlo.new_line()

    # Methode die beschrijft wat de speler in de cel ziet.
    def kijk_rond(self):
        dlo.print_text_dialogue("In je cel heb je een kast,<200> een prullenbak,<200> en je bed.<300>", 1.7)
        dlo.new_line()
        dlo.print_text_dialogue("Ook zit er een klein gat boven je bed.<600>", 1)
        dlo.new_line()

    # Methode om specifieke objecten in de cel te bekijken en ermee te interageren.
    def bekijk_item(self, item_naam):
        # Interactie met de kast.
        if item_naam == "kast":
            if "kast" in self.looted:  # Controleer of de kast al is geplunderd.
                dlo.print_text_dialogue("Dit is een kast.", 0.5)
                dlo.new_line()
                return
            dlo.print_text_dialogue("In de kast zit een zakje muesli. Wil je deze meenemen? (JA/NEE)", 2)
            dlo.new_line()
            meeneem = input(": ").lower()
            if "ja" in meeneem:  # Als de speler ja kiest.
                self.looted.append("kast")  # Markeer de kast als geplunderd.
                self.inventory.append("muesli")  # Voeg muesli toe aan de inventory.
                dlo.print_text_dialogue("Je hebt nu de muesli.", 0.8)
                dlo.new_line()
            elif not "nee" in meeneem:  # Ongeldige invoer.
                dlo.print_text_dialogue("Ongeldige invoer,<300> probeer weer naar dit ding te gaan!", 1.5)
                dlo.new_line()

        # Interactie met de prullenbak.
        if item_naam == "prullenbak":
            if "prullenbak" in self.looted:  # Controleer of de prullenbak al is geplunderd.
                dlo.print_text_dialogue("Dit is een prullenbak.", 0.6)
                dlo.new_line()
                return
            dlo.print_text_dialogue("In de prullenbak zit een hamer. Wil je deze meenemen? (JA/NEE)", 2)
            dlo.new_line()
            meeneem = input(": ").lower()
            if "ja" in meeneem:  # Als de speler ja kiest.
                self.looted.append("prullenbak")  # Markeer de prullenbak als geplunderd.
                self.inventory.append("hamer")  # Voeg de hamer toe aan de inventory.
                dlo.print_text_dialogue("Je hebt nu de hamer.", 0.8)
                dlo.new_line()
            elif not "nee" in meeneem:  # Ongeldige invoer.
                dlo.print_text_dialogue("Ongeldige invoer,<300> probeer weer naar dit ding te gaan!", 1.5)
                dlo.new_line()

        # Interactie met het bed.
        if item_naam == "bed":
            dlo.print_text_dialogue("Dit is je bed.<300> Je bed is erg groot.<500>", 1.5)
            dlo.new_line()
            self.bekijk_item("gat")  # Roep automatisch de interactie met het gat aan.

        # Interactie met het gat.
        if item_naam == "gat":
            dlo.print_text_dialogue(
                "Er zit een klein gat boven je bed.<500> Je kan er deels doorheen kijken en je ziet een lange doorgang.<600>", 2
            )
            dlo.new_line()
            if "hamer" in self.inventory:  # Controleer of de speler een hamer bij zich heeft.
                dlo.print_text_dialogue("Je hebt een hamer bij je.<400> Wil je het gat groter maken? (JA/NEE)", 1.5)
                dlo.new_line()
                meeneem = input(": ").lower()
                if "ja" in meeneem:  # Als de speler ja kiest.
                    dlo.print_text_dialogue(
                        "Het gat is groot genoeg om doorheen te gaan.<600> Je ziet er een lange gang doorheen.<500>", 1.5
                    )
                    dlo.new_line()
                    dlo.print_text_dialogue(
                        "Je gaat door de gang heen,<300> en je komt uit bij een ventilatieschaft.<500>", 1
                    )
                    dlo.new_line()
                    dlo.print_text_dialogue(
                        "Je maakt dit ventilatieschaft open en je komt in een cellencomplex.<1500>", 1.5
                    )
                    dlo.new_line()
                    self.completed = True  # Markeer de scène als voltooid.
                    return
                elif not "nee" in meeneem:  # Ongeldige invoer.
                    dlo.print_text_dialogue("Ongeldige invoer,<300> probeer weer naar dit ding te gaan!", 1.5)
                    dlo.new_line()
            else:  # Als de speler geen hamer heeft.
                dlo.print_text_dialogue(
                    "Misschien kan je dit gat groter maken met een bepaald item,<300> iets van een hamer ofzo.", 2.5
                )
                dlo.new_line()