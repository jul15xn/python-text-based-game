import dialogue as dlo
from scenes.scene import Scene
from scenes import conversation
import os

# Subklasse van Scene, die een specifiek cellencomplex voorstelt.
class Complex(Scene):
    def __init__(self):
        super().__init__()  # Roep de constructor van de basisklasse Scene aan.
        self.in_kamer = False

    # Introductiemethode: wordt geroepen wanneer de speler deze scène betreedt.
    def intro(self):
        dlo.print_text_dialogue(
            "Je bent nu in het cellencomplex.<600>", 0.5
        )
        dlo.new_line()
        self.kijk_rond()
        dlo.print_text_dialogue("Wat wil je doen?<400>", 0.5)
        dlo.new_line()

    # Methode die de speler informatie geeft over de scène wanneer ze rondkijken.
    def kijk_rond(self):
        if self.in_kamer:
            dlo.print_text_dialogue("In de cafetaria staan veel bankjes,<300> en ook een vending machine.<600>", 1.5)
            dlo.new_line()
            dlo.print_text_dialogue("Het lijkt niet of de bankjes iets doen,<300> maar de vending machine wel.<600> Misschien is er wel iets leuks te koop!<600>", 2)
            dlo.new_line()
        else:
            dlo.print_text_dialogue(
                "Je ziet heel veel cellen, <300>en bij de uitgang een bewaker.<600>", 2
            )
            dlo.new_line()
            dlo.print_text_dialogue(
                "Ook zie je een opvallende man die opvallend naar je kijkt.<600>", 1.3
            )
            dlo.new_line()
            dlo.print_text_dialogue(
                "Er is ook een deur aan het begin van het complex.<600>", 1
            )
            dlo.new_line()
            dlo.print_text_dialogue(
                "Omdat je nu door de ventillatieschaft bent gekropen,<300> kan je nu niet meer terug omdat hij te hoog in de gang zit.<600>", 2
            )
            dlo.new_line()


    # Methode waarmee de speler specifieke items of personages in de scène kan bekijken.
    # 'item_naam' is het doelwit dat de speler wil bekijken.
    def bekijk_item(self, item_naam):
        if self.in_kamer:
            if item_naam == "vending machine":
                dlo.print_text_dialogue("Bij de vending machine kan je verschilende dingen kopen:<600>", 1.5)
                dlo.new_line()
                dlo.print_text_dialogue("1. Coca Cola (5 euro)<300>", 0.5)
                dlo.new_line()
                dlo.print_text_dialogue("2. Mystrieus pakketje (2 euro)<300>", 0.5)
                dlo.new_line()
                dlo.print_text_dialogue("3. Sprite (5 euro)<300>", 0.5)
                dlo.new_line()
                dlo.print_text_dialogue("Wat wil je kopen?<600>", 0.8)
                dlo.new_line()
                hoi = input(": ")
                if not hoi.isdigit():
                    dlo.print_text_dialogue("Ongeldige waarde!", 0.5)
                    dlo.new_line()
                elif "1" in hoi or "3" in hoi:
                    dlo.print_text_dialogue("Dit kan je niet betalen!", 0.8)
                    dlo.new_line()
                elif "2" in hoi:
                    if "2 euro" in self.inventory:
                        dlo.print_text_dialogue("Je hebt nu een mystrieus pakketje.<600>", 0.7)
                        dlo.new_line()
                        dlo.print_text_dialogue("Kort nadat je het pakketje hebt gekocht,<300> hoor je een sissend geluid.<600>", 2)
                        dlo.new_line()
                        dlo.print_text_dialogue("En daarna<300>.<300>.<300>.<300>.<1000>", 0.5)
                        dlo.new_line()
                        dlo.print_text_dialogue("BOEM!<600> Hij onploft!<3500>", 0.8)
                        dlo.new_line()
                        os.system("cls")
                        # Eindboodschap en credits.
                        dlo.print_text_dialogue("Je hebt de game uitgespeeld!<400> Bedankt voor het spelen!", 1.5)
                        dlo.new_line()
                        dlo.print_text_dialogue("Dit is 2 van de 2 endings.<400> Dit is de secret ending en er is nog een main ending.<600> Goed gedaan!<10000>", 2.5)
                        dlo.new_line()
                        dlo.print_text_dialogue("Druk op enter om af te sluiten.", 0.8)
                        input()  # Wacht tot de speler op Enter drukt.
                        quit()
                    else:
                        dlo.print_text_dialogue("Dit kan je niet betalen!", 0.8)
                        dlo.new_line()
            if item_naam == "deur":
                self.in_kamer = False
                dlo.print_text_dialogue("Je gaat weer terug naar het cellencomplex.<600>", 1)
                dlo.new_line()
                self.kijk_rond()

        else:
            # Controleer of de speler de man wil bekijken.
            if item_naam == "man":
                output = conversation.man_conv()  # Start de conversatie met de man.
                if output == 69:  # Controleer of een specifieke waarde (bijvoorbeeld '69') is teruggegeven.
                    self.inventory.append("2 euro")  # Voeg 2 euro toe aan de inventory.
                    dlo.print_text_dialogue("Je hebt nu 2 euro!<300>", 0.5)
                    dlo.new_line()
        
            # Controleer of de speler de bewaker wil bekijken.
            if item_naam == "bewaker":
                output = conversation.bewaker_conv(self.inventory)  # Start de conversatie met de bewaker.
                if output == 68:  # Controleer of een specifieke waarde (bijvoorbeeld '68') is teruggegeven.
                    self.completed = True  # Markeer de scène als voltooid.

            # Check of de speler naar de deur wil
            if item_naam == "deur":
                self.in_kamer = True # Markeer dat je in de kamer bent
                dlo.print_text_dialogue("Je opent de deur en je komt in de cafetaria.<600>", 1)
                dlo.new_line()
                self.kijk_rond()