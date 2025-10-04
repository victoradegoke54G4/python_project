import random
mainChoice = ['ROCK', 'PAPER', 'SCISSOR']

def main():
    print('WELCOME TO THE ROCK PAPER SCISSORS GAME.')
    while True:
        '\n'
        userInput = input('Enter your choice (Rock/Paper/Scissor):').upper()
        computerAction = random.choice(mainChoice)
        if not userInput or mainChoice:
            print('Invalid Input.')
        elif userInput == computerAction:
            print('That is a tie. Computer chose {}'.format(computerAction))
        else:
            if userInput == 'ROCK' and computerAction == 'SCISSORS':
                print('You win! Computer chose {}'.format(computerAction))
            elif userInput == 'SCISSOR' and computerAction == 'PAPER':
                print('You win! Computer chose {}'.format(computerAction))
            elif userInput == 'PAPER' and computerAction == 'ROCK' :
                print('You win Computer chose {}'.format(computerAction))
            else:
                print('Oops!. You lose. Computer chose {}'.format(computerAction))
        lastInput = input('Do you want to continue?(y/n): ').lower()
        if lastInput == 'n':
            break
        elif lastInput != ('y' or 'n'):
            print('Check Your Input.')
            quit()
main()