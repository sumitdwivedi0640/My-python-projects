# Function to display the menu options
def print_menu():
    print("1. Convert length")
    print("2. Convert weight")
    print("3. Convert temperature")
    print("4. Exit")

# Function to convert length from meters to feet


def length_converter():
    print("Length Converter")
    length_meters = float(input("Enter length in meters: "))
    length_feet = length_meters * 3.281
    print(f"Length in feet: {length_feet:.2f}")

# Function to convert weight from kilograms to pounds


def weight_converter():
    print("Weight Converter")
    weight_kilograms = float(input("Enter weight in kilograms: "))
    weight_pounds = weight_kilograms * 2.205
    print(f"Weight in pounds: {weight_pounds:.2f}")

# Function to convert temperature from Celsius to Fahrenheit


def temperature_converter():
    print("Temperature Converter")
    temp_celsius = float(input("Enter temperature in Celsius: "))
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {temp_fahrenheit:.2f}")

# Main function to run the unit converter


def main():
    while True:
        print_menu()
        choice = int(input("Select an option: "))

        if choice == 1:
            length_converter()
        elif choice == 2:
            weight_converter()
        elif choice == 3:
            temperature_converter()
        elif choice == 4:
            print("Exiting the unit converter.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Entry point of the program
if __name__ == "__main__":
    main()
