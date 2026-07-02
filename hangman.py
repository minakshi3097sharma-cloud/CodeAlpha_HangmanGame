import random

# Hangman drawings
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Word list
words = [
    "python",
    "computer",
    "keyboard",
    "programming",
    "developer",
    "internet",
    "function",
    "variable",
    "algorithm",
    "software"
]

def play_game():
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("\n================================")
    print("        HANGMAN GAME")
    print("================================")
    print("Guess the word one letter at a time.")
    print("You have 6 wrong attempts.\n")

    while attempts > 0:
        wrong_guesses = 6 - attempts
        print(hangman_stages[wrong_guesses])

        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Attempts left:", attempts)
        print("Guessed letters:", guessed_letters)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!\n")
        else:
            print("Wrong guess!\n")
            attempts -= 1

        all_letters_guessed = True
        for letter in word:
            if letter not in guessed_letters:
                all_letters_guessed = False

        if all_letters_guessed:
            print("\nCongratulations! You won!")
            print("The word was:", word)
            break

    if attempts == 0:
        print(hangman_stages[6])
        print("\nGame Over! You lost.")
        print("The correct word was:", word)

def main():
    while True:
        play_game()

        again = input("\nDo you want to play again? yes/no: ").lower()

        if again != "yes":
            print("Thank you for playing Hangman!")
            break

main()
