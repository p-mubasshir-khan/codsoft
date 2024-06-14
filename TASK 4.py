import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
        if user_choice in ["r", "p", "s"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["r", "p", "s"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "s" and computer_choice == "p") or \
         (user_choice == "p" and computer_choice == "r"):
        return "User wins"
    else:
        return "Computer wins"

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        choices_mapping = {"r": "rock", "p": "paper", "s": "scissors"}
        print(f"\nUser choice: {choices_mapping[user_choice]}")
        print(f"Computer choice: {choices_mapping[computer_choice]}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "User wins":
            user_score += 1
        elif result == "Computer wins":
            computer_score += 1
        print(f"Score - User: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'r' for rock, 'p' for paper, or 's' for scissors to make your choice.")
    play_game()

if __name__ == "__main__":
    main()
