import random
def countries_and_capitals():
    return [
        "Afghanistan | Kabul",
        "Albania | Tirana",
        "Algeria | Algiers",
        "Andorra | Andorra la Vella",
        "Angola | Luanda",
        "Argentina | Buenos Aires",
        "Armenia | Yerevan",
        "Australia | Canberra",
        "Austria | Vienna",
        "Azerbaijan | Baku",
        "Bahamas | Nassau",
        "Bahrain | Manama",
        "Bangladesh | Dhaka",
        "Barbados | Bridgetown",
        "Belarus | Minsk",
        "Belgium | Brussels",
        "Belize | Belmopan",
        "Bhutan | Thimphu",
        "Bolivia | La Paz",
        "Bosnia and Herzegovina | Sarajevo",
        "Botswana | Gaborone",
        "Brazil | Brasilia",
        "Brunei | Bandar Seri Begawan",
        "Bulgaria | Sofia",
        "Burkina Faso | Ouagadougou",
        "Burundi | Bujumbura",
        "Cambodia | Phnom Penh",
        "Cameroon | Yaounde",
        "Canada | Ottawa",
        "Central African Republic | Bangui",
        "Chile | Santiago",
        "China | Beijing",
        "Colombia | Bogota",
        "Costa Rica | San Jose",
        "Croatia | Zagreb",
        "Cuba | Havana",
        "Cyprus | Nicosia",
        "Czech Republic | Prague",
        "Denmark | Copenhagen",
        "Dominican Republic | Santo Domingo",
        "Ecuador | Quito",
        "Egypt | Cairo",
        "Finland | Helsinki",
        "France | Paris",
        "Germany | Berlin",
        "Greece | Athens",
        "Hungary | Budapest",
        "Iceland | Reykjavik",
        "India | New Delhi",
        "Indonesia | Jakarta",
        "Ireland | Dublin",
        "Israel | Jerusalem",
        "Italy | Rome",
        "Japan | Tokyo",
        "Kazakhstan | Astana",
        "Kenya | Nairobi",
        "Latvia | Riga",
        "Lithuania | Vilnius",
        "Luxembourg | Luxembourg",
        "Mexico | Mexico City",
        "Netherlands | Amsterdam",
        "Norway | Oslo",
        "Poland | Warsaw",
        "Portugal | Lisbon",
        "Romania | Bucharest",
        "Spain | Madrid",
        "Sweden | Stockholm",
        "Switzerland | Bern",
        "Turkey | Ankara",
        "Ukraine | Kyiv",
        "United Kingdom | London",
        "United States of America | Washington"
    ]

HANGMANPICS = [
    """
 +---+
 |   |
     |
     |
     |
     |
=======
""",
    """
 +---+
 |   |
 O   |
     |
     |
     |
=======
""",
    """
 +---+
 |   |
 O   |
 |   |
     |
     |
=======
""",
    """
 +---+
 |   |
 O   |
/|   |
     |
     |
=======
""",
    """
 +---+
 |   |
 O   |
/|\  |
     |
     |
=======
""",
    """
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=======
""",
    """
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=======
"""
]
def choose_difficulty():
    print("Choose difficulty: easy / medium / hard")
    while True:
        choice = input(">").lower()
        if choice in ("easy", "medium", "hard"):
            return choice
        print("Invalid difficulty.")


def get_lives(difficulty):
    return {"easy": 6, "medium": 5, "hard": 4}[difficulty]
def choose_word_by_difficulty(difficulty):
    words = []
