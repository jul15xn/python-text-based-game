import dialogue as dlo

MAN_CONV = [
    {
        "text": "Yo man. Wat moet je?",
        "antwoorden": [
            {
                "text": "Hoe gaat het?",
                "jump": 1
            },
            {
                "text": "Wil je gepijpt worden?",
                "jump": 2
            },
            {
                "text": "Doei.",
                "jump": -1
            }
        ]
    },
    {
        "text": "Met mij gaat het best, met jouw?",
        "antwoorden": [
            {
                "text": "Wil je gepijpt worden?",
                "jump": 2
            },
            {
                "text": "Doei.",
                "jump": -1
            }
        ]
    },
        {
        "text": "Nou, eigenlijk wel! Kun je me daarmee helpen? Ik geef je er 2 euro voor!",
        "antwoorden": [
            {
                "text": "Is goed!",
                "jump": 3
            },
            {
                "text": "Laat maar...",
                "jump": -1
            },
        ]
    },
        {
        "text": "Bedankt voor het helpen! Hier heb je 2 euro.",
        "antwoorden": [
            {
                "text": "*neem de 2 euro*",
                "jump": 69
            }
        ]
    }
]

def list_conv(item, name):
    print(dlo.DOCENT.parseText(f"{name}: {item["text"]}"))
    print('')
    for i in range(len(item["antwoorden"])):
        print(dlo.DOCENT.parseText(f"{i+1}. {item["antwoorden"][i]["text"]}"))

    choise = input("> ")
    choise = int(choise)-1

    ranges = range(len(item["antwoorden"]))
    if choise in ranges:
        return item["antwoorden"][choise]["jump"]

def man_conv():
    conv = MAN_CONV
    ix = 0
    iy = 0
    while True:
        iy = ix
        iy = list_conv(conv[iy], "MAN")
        if iy == -1 or iy:
            break