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

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

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

    for entry in countries_and_capitals():
        country = entry.split(" | ")[0]
        length = sum(1 for c in country if c.isalpha())

        if difficulty == "easy" and length <= 7:
            words.append(country)
        elif difficulty == "medium" and 8 <= length <= 10:
            words.append(country)
        elif difficulty == "hard" and length >= 11:
            words.append(country)

    return random.choice(words)

def display_state(word, revealed, wrong_letters, lives, max_lives):
    print(HANGMANPICS[max_lives - lives])
    print("Word: ", end="")

    for c in word:
        if not c.isalpha() or c.lower() in revealed:
            print(c, end=" ")
        else:
            print("_", end=" ")

    print("\n")

    if wrong_letters:
        print("Wrong letters:", ", ".join(sorted(wrong_letters)))

    print(f"Lives left: {lives}")
    print("-" * 30)

def get_guess(guessed_letters):
    guess = input("Guess a letter (or 'quit'): ").strip()

    if guess.lower() == "quit":
        return "quit"

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter ONE letter.")
        return None

    guess = guess.lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        return "repeat"

    return guess


def check_win(word, revealed):
    return all(
        not c.isalpha() or c.lower() in revealed
        for c in word
    )

def play_game():
    difficulty = choose_difficulty()
    max_lives = get_lives(difficulty)
    lives = max_lives
    word = choose_word_by_difficulty(difficulty)

    revealed_letters = set()
    wrong_letters = set()
    guessed_letters = set()

    print(f"\n🌍 HANGMAN – Difficulty: {difficulty.upper()} 🌍\n")

    while True:
        display_state(word, revealed_letters, wrong_letters, lives, max_lives)

        guess = get_guess(guessed_letters)

        if guess == "quit":
            print("Good-bye!")
            break
        if guess in (None, "repeat"):
            continue

        guessed_letters.add(guess)

        if guess in word.lower():
            revealed_letters.add(guess)
            if check_win(word, revealed_letters):
                display_state(word, revealed_letters, wrong_letters, lives, max_lives)
                print("🎉 YOU WIN! 🎉")
                break
        else:
            wrong_letters.add(guess)
            lives -= 1
            if lives == 0:
                print(HANGMANPICS[-1])
                print(f"💀 YOU LOST! The country was: {word}")
                break

if __name__ == "__main__":
    play_game()