import random

word_list = ["python", "hangman", "programming",
             "computer", "language", "game"]


def choose_word():
    return random.choice(word_list)


def hangman():
    chosen_word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        display = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"

        print(display)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in chosen_word:
            guessed_letters.append(guess)
            if display == chosen_word:
                print(
                    f"Congratulations! You've guessed the word: {chosen_word}")
                break
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Game over! The word was {chosen_word}.")


if __name__ == "__main__":
    hangman()
