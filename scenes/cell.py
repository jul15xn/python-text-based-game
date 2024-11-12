import dialogue as dlo
import time

def cell(docentmode):
    dlo.print_text_dialogue("Je bent in een cel in de gevangenis.<600>", 2)
    dlo.new_line()
    dlo.print_text_dialogue("Hier ben je beland door het proberen te bestelen van de juwelier.<600>", 3)
    dlo.new_line()
    dlo.print_text_dialogue("Nu wil je proberen te ontsnappen uit de gevangenis.<600>", 2)
    dlo.new_line()
    dlo.print_text_dialogue("In je cel heb je een kast,<200> een prullenbak,<200> en je bed.<600>", 3)
    time.sleep(1)
    dlo.new_line()
    dlo.print_text_dialogue("Wat wil je nu gaan doen?<500>", 1)
    dlo.new_line()