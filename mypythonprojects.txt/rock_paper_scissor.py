import random  # Import the random module to generate computer's choice

# Function to get the user's choice


def get_user_choice():
    while True:
        # Get user's choice and convert to lowercase
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

# Function to get the computer's random choice


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner of the game


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif user == "rock":
        return "You win!" if computer == "scissors" else "Computer wins!"
    elif user == "paper":
        return "You win!" if computer == "rock" else "Computer wins!"
    elif user == "scissors":
        return "You win!" if computer == "paper" else "Computer wins!"

# Function to ask if the user wants to play again


def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

# Main function to run the game


def main():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice()  # Get user's choice
        computer_choice = get_computer_choice()  # Get computer's choice

        print(f"You chose {user_choice}. Computer chose {computer_choice}.")

        result = determine_winner(
            user_choice, computer_choice)  # Determine the winner
        print(result)

        if not play_again():  # Ask if the user wants to play again
            print("Thanks for playing!")
            break


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
