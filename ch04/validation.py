#!/usr/bin/env python3

def get_float(message, low, high):
    while True:
        value = float(input(message))
        if value <= low or value > high:
            print("Entry must be greater than " + str(low) + " or less than or equal than " + str(high))
        else:
            return value

def get_int(message, low, high):
    while True:
        value = int(input(message))
        if value <= low or value > high:
            print("Entry must be greater than " + str(low) + " or less than or equal than " + str(high))
        else:
            return value

def main():
    choice = "y"
    while choice.lower() == "y":
        # test the get_float method
        test = get_float("Please enter real number between 0 and 100: ", 0, 100)

        # test the get_int method
        test = get_int("Please enter integer between 0 and 100: ", 0, 100)

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
