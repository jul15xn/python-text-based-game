import dialogue as dlo
import os

MAN_CONV = [
    {
        "text": "Yo man. Wat moet je?",
        "antwoorden": [
            {
                "text": "Hoe gaat het?",
                "jump": 1
            },
            {
                "text": "Je kamer is echt een puinhoop...",
                "jump": 2
            },
            {
                "text": "Niks, doei.",
                "jump": -1
            }
        ]
    },
    {
        "text": "Met mij gaat het wel prima. En met jou?",
        "antwoorden": [
            {
                "text": "Ook wel goed, maar serieus, die kamer van je...",
                "jump": 2
            },
            {
                "text": "Geen tijd voor small talk, doei.",
                "jump": -1
            }
        ]
    },
    {
        "text": "Ja, ja, ik weet het. Het is een rommel. Maar ja, opruimen is niet echt mijn ding...",
        "antwoorden": [
            {
                "text": "Kan ik je helpen opruimen?",
                "jump": 3
            },
            {
                "text": "Nou, dat zie ik... succes ermee.",
                "jump": -1
            }
        ]
    },
    {
        "text": "Echt? Dat zou geweldig zijn! Samen is het sneller gedaan.",
        "antwoorden": [
            {
                "text": "*ga helpen met opruimen*",
                "jump": 4
            },
            {
                "text": "Hmm, toch geen zin. Laat maar.",
                "jump": -1
            }
        ]
    },
    {
        "text": "Wow, bedankt voor de hulp! Het ziet er hier eindelijk een beetje netjes uit. Hier, een kleine beloning: 2 euro!",
        "antwoorden": [
            {
                "text": "*neem de 2 euro*",
                "jump": 69
            },
            {
                "text": "Dat is niet nodig, maar bedankt!",
                "jump": -1
            }
        ]
    }
]

BEWAKER_CONV = [
    {
        "text": "Hallo daar. Is er iets?",
        "antwoorden": [
            {
                "text": "Hoe gaat het ermee?",
                "jump": 1
            },
            {
                "text": "Krijg de tiefus!",
                "jump": 2
            },
            {
                "text": "Doei.",
                "jump": -1
            }
        ]
    },
    {
        "text": "Met mij gaat het prima.",
        "antwoorden": [
            {
                "text": "Mag ik eruit?",
                "jump": 3
            },
            {
                "text": "Doei.",
                "jump": -1
            }
        ]
    },
    {
        "text": "Wat onbeschoft! Je mag er zeker niet uit.",
        "antwoorden": [
            {
                "text": "Sorry...",
                "jump": 1
            },
            {
                "text": "Doei.",
                "jump": -1
            }
        ]
    },
    {
        "text": "Helaas, ik kan je er niet zomaar uitlaten.",
        "antwoorden": [
            {
                "text": "Wat heb je nodig om me eruit te laten?",
                "jump": 4
            },
            {
                "text": "Doei.",
                "jump": -1
            }
        ]
    },
    {
        "text": "Tja... misschien een lekker bakje muesli? Heb je dat?",
        "antwoorden": [
            {
                "text": "Hier is een bakje muesli.",
                "jump": 5,
                "requires": "muesli"
            },
            {
                "text": "Nee, helaas niet.",
                "jump": 6
            }
        ]
    },
    {
        "text": "Ah, geweldig! Je mag eruit. Goede reis!",
        "antwoorden": [
            {
                "text": "Bedankt!",
                "jump": 68
            }
        ]
    },
    {
        "text": "Oh, dat is jammer. Misschien kom je terug als je muesli hebt.",
        "antwoorden": [
            {
                "text": "Oké, ik kom terug.",
                "jump": -1
            }
        ]
    }
]

# Functie om een lijst met conversatieopties te tonen en een keuze te maken.
# 'item' is het huidige deel van de conversatie (met tekst en antwoorden).
# 'name' is de naam van de spreker.
# 'inventory' is optioneel en bevat de items die de speler bezit.
def list_conv(item, name, inventory=None):
    os.system("cls")  # Maak het scherm leeg voor een schone presentatie.
    print(f"{name}: {item['text']}")  # Toon de naam van de spreker en hun tekst.
    print('')
    
    valid_options = []  # Lijst met beschikbare antwoorden.

    # Loop door alle antwoorden en controleer eventuele vereisten.
    for idx, option in enumerate(item["antwoorden"]):
        requires = option.get("requires")  # Vereist dit antwoord een item?
        if requires and inventory and requires not in inventory:  # Als een item vereist is en ontbreekt, sla het over.
            continue
        valid_options.append(option)  # Voeg het antwoord toe aan de lijst met geldige opties.
        print(f"{len(valid_options)}. {option['text']}")  # Print het antwoord met een nummer.

    # Als er geen geldige opties zijn, sluit de conversatie af.
    if not valid_options:
        print("Geen opties beschikbaar. Druk op Enter om af te sluiten.")
        input("> ")  # Wacht op de speler.
        return -1  # Geef -1 terug om de conversatie te beëindigen.

    dlo.new_line()  # Print een lege regel.

    while True:
        choice = input("> ")  # Vraag de speler om een keuze.
        if not choice.isdigit():  # Controleer of de input een geldig getal is.
            print("Ongeldige invoer. Voer een geldig getal in.")
            continue

        choice = int(choice) - 1  # Converteer input naar een index.

        if 0 <= choice < len(valid_options):  # Controleer of de keuze geldig is.
            return valid_options[choice]["jump"]  # Geef de 'jump'-waarde terug (volgend deel van de conversatie).
        else:
            print("Ongeldige keuze. Kies een geldig nummer.")

# Functie die een hele conversatie doorloopt op basis van een gestructureerde 'conv'-lijst.
# 'conv' is een lijst met conversatiestappen, elk met tekst en antwoorden.
# 'name' is de naam van de spreker.
# 'inventory' bevat optioneel de items die de speler bezit.
def do_conversation(conv, name, inventory=None):
    iy = 0  # Start bij het eerste deel van de conversatie.
    while True:
        iy = list_conv(conv[iy], name, inventory)  # Toon een deel van de conversatie en krijg de volgende index.
        if iy == -1 or iy >= len(conv):  # Stop als de conversatie eindigt of de index ongeldig is.
            break

    return iy  # Geef de laatste index terug.

# Specifieke functie voor de conversatie met een man.
def man_conv():
    return do_conversation(MAN_CONV, "MAN")

# Specifieke functie voor de conversatie met een bewaker.
# 'inventory' wordt doorgegeven om opties afhankelijk te maken van de items die de speler heeft.
def bewaker_conv(inventory):
    return do_conversation(BEWAKER_CONV, "BEWAKER", inventory)