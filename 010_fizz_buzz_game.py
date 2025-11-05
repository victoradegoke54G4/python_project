'''Welcome To The Fizz Buzz Game.'''

def main():

    for number in range (0,101):
        
        if number % 5 == 0 and number % 7 == 0:
            print('Fizz Buzz')
        elif number % 5 == 0:
            print('Fizz')
        elif number % 7 == 0:
            print('Buzz')
        else:
            print(number)

main()