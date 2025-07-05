import random
from Hangman import display_hangman

def hangman_quiz():
    questions = [
        ("What is the national animal of India?", "tiger"),
        ("What is the national bird of India?", "peacock"),
        ("What is the capital of India?", "delhi"),
        ("Which river is considered the holiest in India?", "ganga"),
        ("Who was the first Prime Minister of India?", "nehru"),
        ("Which is the largest state in India by area?", "rajasthan")
    ]

    question, answer = random.choice(questions)
    answer = answer.lower()
    attempts = 6
    guessed_letters = set()
    correct_letters = set()

    print(" Welcome to the Hangman Quiz!")
    print(" Question:", question)
    print(f"You have {attempts} wrong guesses allowed.\n")

    while attempts > 0:
        display_hangman(6 - attempts)

        # Display the current guess progress
        display = ""
        for letter in answer:
            if letter in correct_letters:
                display += letter + " "
            else:
                display += "_ "
        print("\nAnswer:", display.strip())

        # Check if player has guessed all letters
        if set(answer) == correct_letters:
            print("\n Congratulations! You guessed the correct answer!")
            break

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print(" You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            print(" Good guess!")
            correct_letters.add(guess)
        else:
            attempts -= 1
            print(f" Wrong guess! Attempts left: {attempts}")

    else:
        display_hangman(6)
        print(f"\n Sorry, you lost. The correct answer was '{answer}'.")

if __name__ == "__main__":
    hangman_quiz()
