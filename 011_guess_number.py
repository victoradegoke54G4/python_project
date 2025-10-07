import math
import random

def get_int(prompt):
    # if not prompt or not isinstance(prompt, str):
    #      print('Check Input')
    # else:
    while True:
        try:
            return int(input(prompt))
        
        except (ValueError, TypeError):
            print('Invalid Input')
            quit()

def get_chances(p_l_band, p_u_band):
    return int(math.log(p_u_band - p_l_band + 1,2))

def main():

    lower_band = get_int('Enter Lower Band: ')
    upper_band = get_int('Enter Upper Band: ')

    print('\n\tYou have only {} chances'.format(get_chances(lower_band,upper_band)))

    chances= get_chances(lower_band,upper_band)
    computerGuess = random.randint(lower_band,upper_band)
    while True: 
        userGuess = get_int('Guess The Number: ')
        chances -=1 
        if chances == 0:
            print('Oops! You lost.')
            break
        if userGuess == computerGuess:
            print('Welldone! You won the game.')
            break
        elif userGuess> computerGuess:
            print('You Guessed too High')
            print(' You have {} chances.'.format(chances))
        elif userGuess < computerGuess:
            print('You Guessed too Low')
            print('You have {} chances.'.format(chances))
main()