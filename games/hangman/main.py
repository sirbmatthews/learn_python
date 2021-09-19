from hangman_art import logo, stages
from hangman_words import word_list
import random

def printLogo():
    print(logo)

def check_repeated_letter(guess, guessed_letters):
    """Checks if the guessed letter was already guessed before."""
    if guess in guessed_letters:
            print(f"You already guessed {guess}")

def verify_letter_guess(chosen_word, guess, display):
    """Checks if the guessed letter is part of the word and returns the updated user's displayed guessed word."""
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    return display

def update_game_status(guess, chosen_word, guessed_letters, lives, end_of_game, display):
    """Checks the status of the game, returns the the updated number of lives and the upadated status of the game."""
    if guess not in chosen_word and guess not in guessed_letters:
        print(f"you guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    elif "_" not in display:
        end_of_game = True
        print("You win.")
                
    return end_of_game, lives

def startGame():
    chosen_word = random.choice(word_list)
    end_of_game = False
    lives = 6
    display = []
    guessed_letters = []

    printLogo()

    for _ in range(len(chosen_word)):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        while len(guess) is not 1 or not guess.isalpha():
            guess = input("Guess a single letter [A-z]: ").lower()

        check_repeated_letter(guess, guessed_letters)        
        display = verify_letter_guess(chosen_word, guess, display)
        end_of_game, lives = update_game_status(guess, chosen_word, guessed_letters, lives, end_of_game, display)
        print(f"{' '.join(display)}")
        print(stages[lives])
        guessed_letters.append(guess)

    print(f"The word is {chosen_word}")

if __name__ == '__main__':
    startGame()
    