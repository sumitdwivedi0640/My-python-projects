from random import randint #It is built-in function of random module in Python that returns random integer b/w the higher and lower limit passed as parameters.

lower_number=1
Higher_number=100  # Define the range of possible numbers

random_number:int = randint(lower_number,Higher_number) # Generate a random number within the specified range
print(f"Guess the number between {lower_number} and {Higher_number}")

while True:
    try:
        user_guess=int(input("Guess: "))
    except ValueError as e:
        print("Enter the valid number: ")
        continue

    if user_guess > random_number:
        print("The number is lower:")
    elif user_guess < random_number:
        print("The number is higher: ")
    else:
        print("You guessed it!")
        break
