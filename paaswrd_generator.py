import random

# Function to generate a random password
def generate_password(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?~"  # All possible characters for the password
    password = "".join(random.choice(characters) for _ in range(length))  # Join randomly selected characters to form the password
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    password = generate_password(length)  # Generate the password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
