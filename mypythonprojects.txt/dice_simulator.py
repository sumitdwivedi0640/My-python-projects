import random

# Function to simulate rolling dice
def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError("Amount of dice must be a positive integer.")
    
    rolls_list: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)  # Generate a random number between 1 and 6
        rolls_list.append(random_roll)  # Add the roll result to the list
    
    return rolls_list

# Main game loop
def main():
    while True:
        try:
            user_input_str: str = input("How many dice to roll? ")

            if user_input_str.lower() == "exit":
                print("Thanks for playing!")
                break

            # Call the roll_dice function and unpack its results using * (unpacking operator)
            print(*roll_dice(int(user_input_str)), sep=",")
        except ValueError:
            print("Please enter a valid number")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
