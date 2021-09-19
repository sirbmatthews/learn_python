import os
from art import logo
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Selects a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return int(random.choice(cards))

def compute_score(cards):
    """Calculates and updates the user or computer scores."""
    return int(sum(cards))

def current_state(user_cards, user_score, computer_cards):
    """Prints the current game status."""
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

def final_state(user_cards, user_score, computer_cards, computer_score):
    """Prints the finl status of the game."""
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

def check_blackjack(user_score, computer_score):
    """Checks if the user or the computer don't possess a blackjack."""
    if user_score != 21 or computer_score != 21:
        return False
    else:
        if user_score == 21:
            print("Win with a Blackjack 😎")
        elif computer_score == 21:
            print("Lose, opponent wins with a Blackjack")
        return True

def play_computer(computer_cards, computer_score):
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = compute_score(computer_cards)
    return computer_cards, computer_score

def compare_scores(user_cards, user_score, computer_cards, computer_score):
    """Compares the scores and outputs the final status of the game."""
    final_state(user_cards, user_score, computer_cards, computer_score)
    if computer_score < user_score:
        print("You win 😃")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif computer_score == user_score:
        print("Draw 🙃")
    else:
        print("You lose 😤")

def check_for_ace(cards, score):
    """Check if the user or computer cards contain Ace and if the score is greater than 21, convert it from 11 to 1."""
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return cards

def play_game():
    """Game controller function."""
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    clear()
    print(logo)

    end_of_game = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        user_score = compute_score(user_cards)
        computer_score = compute_score(computer_cards)
    
    current_state(user_cards, user_score, computer_cards)
    end_of_game = check_blackjack(user_score, computer_score)
    
    while not end_of_game:
        getAnotherCard = input("Type 'y' to get another card, type any other key(s) to pass: ")
        if getAnotherCard == "y" or getAnotherCard == "Y":
            user_cards.append(deal_card())
            user_score = compute_score(user_cards)
            user_cards = check_for_ace(user_cards, user_score)
            if user_score > 21:
                computer_cards, computer_score = play_computer(computer_cards, computer_score)
                computer_cards = check_for_ace(computer_cards, computer_score)
                final_state(user_cards, user_score, computer_cards, computer_score)
                print("You went over, you lose 😭")
                end_of_game = True
            else:
                current_state(user_cards, user_score, computer_cards)
        else:
            computer_cards, computer_score = play_computer(computer_cards, computer_score)
            computer_cards = check_for_ace(computer_cards, computer_score)
            compare_scores(user_cards, user_score, computer_cards, computer_score)
            end_of_game = True

if __name__ == '__main__':
    start_game = True
    while start_game:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play == "y" or play == "Y":
            play_game()
        else:
            start_game = False
