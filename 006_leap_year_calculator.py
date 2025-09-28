
def main():
    print('Welcome to the Ultimate Leap Year Calculator.')
    userInput = int(input('Enter year you would like to verify: '))
    if userInput > 0:
        if userInput % 4 == 0:
            if userInput % 100 == 0:
                if userInput % 400 == 0:
                    print('Number is a leap year.')
                else:
                    print('Number is not a leap year.')
            else:
                print('Number is a leap year')
        else:
            print('Number is not a leap year')
    else:
        print('Invalid Input')
main()