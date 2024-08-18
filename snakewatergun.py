# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.

import random
import time

# Constants for choices
SNAKE = 'S'
WATER = 'W'
GUN = 'G'
CHOICES = [SNAKE, WATER, GUN]

# Win conditions mapped in a dictionary
WIN_CONDITIONS = {
    SNAKE: WATER,
    WATER: GUN,
    GUN: SNAKE
}

def get_user_choice():
    user = input("Enter your choice (S for Snake, W for Water, G for Gun): ").upper()
    while user not in CHOICES:
        print("Invalid choice! Please enter S, W, or G.")
        user = input("Enter your choice (S for Snake, W for Water, G for Gun): ").upper()
    return user

def determine_winner(computer, user):
    if user == computer:
        return "tie"
    elif WIN_CONDITIONS[user] == computer:
        return "win"
    else:
        return "lose"

def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0
    ties = 0

    while True:
        computer = random.choice(CHOICES)
        user = get_user_choice()
        result = determine_winner(computer, user)
        
        if result == "tie":
            print(f"Game Tie! You choose {user} and the computer choose {computer}.")
            ties += 1
        elif result == "win":
            print(f"You Win! You choose {user} and the computer choose {computer}.")
            user_score += 1
        else:
            print(f"You Lose! You choose {user} and the computer choose {computer}.")
            computer_score += 1

        # Display the current score
        print(f"\nScore: You {user_score} - Computer {computer_score} - Ties {ties}")

        # Ask the user if they want to play again
        replay = input("\nDo you want to play again? (Y/N): ").upper()
        if replay != 'Y':
            print("\nThanks for playing!")
            print(f"Final Scores:\nYou: {user_score}\nComputer: {computer_score}\nTies: {ties}")
            break

        # Time delay between rounds for better pacing
        time.sleep(1.5)

if __name__ == "__main__":
    play_game()
