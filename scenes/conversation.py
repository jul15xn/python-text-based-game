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

def list_conv(item, name, inventory=None):
    print(f"{name}: {item['text']}")
    print('')
    valid_options = []

    for idx, option in enumerate(item["antwoorden"]):
        requires = option.get("requires")
        if requires and inventory and requires not in inventory:
            continue
        valid_options.append(option)
        print(f"{len(valid_options)}. {option['text']}")

    if not valid_options:
        print("Geen opties beschikbaar. Druk op Enter om af te sluiten.")
        input("> ")
        return -1
    
    dlo.new_line()

    choice = input("> ")
    choice = int(choice) - 1

    if 0 <= choice < len(valid_options):
        return valid_options[choice]["jump"]
    else:
        return -1
    
def do_conversation(conv, name, inventory=None):
    iy = 0
    while True:
        iy = list_conv(conv[iy], name, inventory)
        if iy == -1 or iy >= len(conv):
            break

    return iy  

def man_conv():
    return do_conversation(MAN_CONV, "MAN")

def bewaker_conv(inventory):
    return do_conversation(BEWAKER_CONV, "BEWAKER", inventory)