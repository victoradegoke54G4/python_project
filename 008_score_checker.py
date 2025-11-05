
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Invalid Value.')
        except TypeError:
            print('Check Type Input.')

def main():
    '''Allows user to interact with code'''
    userInput = get_float('Enter Score in the range of (0.0 - 1.0): ')

    for num in range(0, 1):
        try:
            if userInput >= 0.9:
                print('A')
            elif userInput >= 0.8:
                print('B')
            elif userInput >= 0.7:
                print('C')
            elif userInput >= 0.6:
                print('D')
            elif userInput < 0.6:
                print('F')
            else:
                print('Wrong Input')
        except TypeError:
            print('Check Type Input.')

main()