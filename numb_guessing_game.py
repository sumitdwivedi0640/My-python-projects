from random import randint  # Import the randint function from the random module

lower_limit = 1
higher_limit = 100  # Define the range of possible numbers

random_number = randint(lower_limit, higher_limit)  # Generate a random number within the specified range
print(f"Guess the number between {lower_limit} and {higher_limit}")

while True:
    try:
        user_guess = int(input("Guess: "))  # Get user's guessed number
    except ValueError:
        print("Enter a valid number.")
        continue

    if user_guess > random_number:
        print("The number is lower.")
    elif user_guess < random_number:
        print("The number is higher.")
    else:
        print("You guessed it!")
        break
