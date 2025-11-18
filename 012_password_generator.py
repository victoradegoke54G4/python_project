import random
letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
numbers = '0123456789'
symbols = '!"£$%^&*_+:@~?¬'

password = ''
def password_gen(main,input):
    global password
    for x in range(1,input+1):
        password += random.choice(main)
    
def main ():
    
    letterInput = int(input(('Enter amount of letters you want in password: ')))
    numberInput = int(input('Enter amount of numbers you want in password: '))
    symbolInput = int(input('Enter amount of symbols you want in password: '))

    password_gen(letters, letterInput)
    password_gen(numbers,numberInput)
    password_gen(symbols,symbolInput)
    
    print(f'Your password is: {password}')

    password_list = list(password)
    random.shuffle(password_list)
    # print(f'Your password is: {password_list}')

    adv_password = ' , '.join(password_list)

    print(f'Your advanced password is: {adv_password}')

main()