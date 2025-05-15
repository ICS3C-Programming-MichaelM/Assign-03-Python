#!/usr/bin/env python3

# Created By: Micthelle Michael
# Date: may 13, 2025
# This program calculates the average of a list of numbers.


def main():
    # this line of code prints out the welcome message
    print("This program calculates the average of a list of numbers.")
    # this line of code gets the input for number 1
    number_1 = input("Enter a number 1: ")
    # this line of code gets the input for number 2
    number_2 = input("Enter a number 2: ")
    # this line of code gets the input for number 3
    number_3 = input("Enter a number 3: ")
    try:
        # this line of code converts the input to a float
        number_1 = int(number_1)
        number_2 = int(number_2)
        number_3 = int(number_3)
        # Checks if numbers are lower than 100 and mopre than 0
        try:
            number_1 < 100 and number_1 > 0
            number_2 < 100 and number_2 > 0
            number_3 < 100 and number_3 > 0
            # this line of code calculates the average
            average = (number_1 + number_2 + number_3) / 3
            # this line of code prints out the average
            print("Average = {}".format(average))
        except Exception:
            # if numbers are not between 0 and 100 types the message
            print("Please enter numbers between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
# # this line of code prints out the average
#     print("Average = {}".format(average))
