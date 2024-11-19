import os
import sys
import time
import re
import colors as cs

# Functie om tekst langzaam te printen, met optie voor kleurtags en vertragingstijd.
def print_text_dialogue(text, total_intro_time, fore=37, back=40):
    # Split de tekst in delen op basis van tags zoals <100> (geeft milliseconden aan).
    parts = re.split(r'(<\d+>)', text)
    
    # Verwijder alle vertragingstags uit de tekst om het aantal karakters te tellen.
    text_only = re.sub(r'<\d+>', '', text)
    # Bereken hoe lang elk karakter apart moet duren.
    separate_sleep_time = total_intro_time / len(text_only)

    # Stel de tekstkleur en achtergrondkleur in.
    cs.set_console_color(fore, back)
    
    # Loop door elk deel van de tekst.
    for part in parts:
        if re.match(r'<\d+>', part):  # Als het deel een vertragingstag is, haal de tijd op.
            delay = int(part[1:-1]) / 1000  # Tag is in milliseconden; omzetten naar seconden.
            time.sleep(delay)  # Pauzeer voor de opgegeven tijd.
        else:  # Voor gewone tekst zonder tags.
            for letter in part:  # Print de tekst letter voor letter.
                print(letter, end='', flush=True)  # Blijf op dezelfde regel en forceer output.
                if True:  # Voor het testen van de game, als je dit op false zet, is er geen delay tussen de karakters
                    time.sleep(separate_sleep_time)

# Print een nieuwe lege regel.
def new_line():
    print("")