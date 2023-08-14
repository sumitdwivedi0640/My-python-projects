import time

# Function to start the countdown timer
def countdown_timer(seconds):
    for i in range(seconds, 0, -1):  # Loop from the specified seconds down to 1
        print(f"Time remaining: {i} seconds")
        time.sleep(1)  # Pause the program for 1 second

    print("Time's up!")

def main():
    print("Welcome to the Countdown Timer!")

    try:
        seconds = int(input("Enter the number of seconds to count down: "))
        if seconds <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    countdown_timer(seconds)  # Start the countdown timer

if __name__ == "__main__":
    main()
