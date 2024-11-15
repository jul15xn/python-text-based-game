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
                "text": "Wat ziet je kamer er rommelig uit...",
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
                "text": "Wat ziet je kamer er rommelig uit...",
                "jump": 2
            },
            {
                "text": "Doei.",
                "jump": -1
            }
        ]
    },
    {
        "text": "Ja dat klopt, ik moet hem nog opruimen...",
        "antwoorden": [
            {
                "text": "Heb je hulp nodig?",
                "jump": 3
            },
            {
                "text": "Doei.",
                "jump": -1
            },
        ]
    },
    {
        "text": "Als je wilt helpen mag dat altijd!",
        "antwoorden": [
            {
                "text": "*ga helpen met opruimen*",
                "jump": 4
            },
            {
                "text": "Laat maar...",
                "jump": -1
            }
        ]
    },
    {
        "text": "Bedankt voor het helpen! Als bedankje krijg je van mij 2 euro.",
        "antwoorden": [
            {
                "text": "*neem de 2 euro*",
                "jump": 69
            }
        ]
    }
]

def list_conv(item, name):
    print(f"{name}: {item["text"]}")
    print('')
    for i in range(len(item["antwoorden"])):
        print(f"{i+1}. {item["antwoorden"][i]["text"]}")

    choise = input("> ")
    choise = int(choise)-1

    ranges = range(len(item["antwoorden"]))
    if choise in ranges:
        return item["antwoorden"][choise]["jump"]

def man_conv():
    conv = MAN_CONV
    iy = 0
    while True:
        iy = list_conv(conv[iy], "MAN")
        if iy == -1 or iy > len(conv):
            break

    return iy