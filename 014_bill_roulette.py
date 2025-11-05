import random

def bill_roulette(p_userInput):
    '''returns a random name from list of name inputs'''
    userInput_list = p_userInput.split(',')
    usernNames = random.choice(userInput_list)
    return usernNames


def main():
    '''allows user to interact with the app'''

    print ('WELCOME TO THE BILL ROULETTE APP')
    while True:
        print()
        print('Who\'s paying the meal today? Enter \'quit\' to leave the app')
        usernameInput= input('Enter your names seperated by a comma: ').upper()
        if not usernameInput or usernameInput.isdigit():
            print('Check Your Input.')
        elif usernameInput == 'QUIT':
            break
        else:
            result = bill_roulette(usernameInput)
            print('{} is buying the food today.'.format(result))
            if result:
                t =input('Do you want to continue?y/n: ').upper()
                if t == 'N':
                        break
                
    print('\nThank You For Using The App')
main()

