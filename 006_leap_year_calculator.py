def get_int(prompt):
    """Converts string type to float with exception handling"""
    while True:
        try:
            return int(float(input(prompt)))
        except ValueError:
            print("Invalid Input")


def main():
    """Allows User Interaction With Code"""

    print("Welcome to the Ultimate Leap Year Calculator.")
    userInput = get_int("Enter year you would like to verify: ")
    try:
        if userInput > 0:
            if userInput % 4 == 0:
                if userInput % 100 == 0:
                    if userInput % 400 == 0:
                        print("Number is a leap year.")
                    else:
                        print("Number is not a leap year.")
                else:
                    print("Number is a leap year")
            else:
                print("Number is not a leap year")
        else:
            print("Invalid Input")
    except TypeError:
        return "Wrong Type Input."


main()
