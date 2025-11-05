import re

def password_detector(password):

    letterl = re.search(r'[a-z]+', password)
    letteru = re.search(r'[A-Z]+', password)
    digit = re.search(r'[0-9]+', password)
    symbol = re.search(r'[@#~?/><|+=_)(*&^%$£"!¬)-]+', password)

    if not letterl:
        print('Your password must contain one or more lowercase letters')
        return 0
    if not letteru:
        print('Your password must contain one or more uppercase letters')
        return 0
    if not digit:
        print('Your password must contain one or more number')
        return 0
    if not symbol:
        print('Your password must contain one or more ssymbols')
        return 0
    return 1



def main():
    """Display user Interface"""
    print('='*20)
    print('Let\'s Check Your Password\'s strength.')
    print('Type Q to quit')
    while True:
        user_input = input('\nEnter Your Password: ')
        if user_input.lower() == 'q':
            break

        if len(user_input) < 8:
            print('❌ Password must be at least 8 characters long.')
            continue

        if password_detector(user_input):    
            print('Your password is strong')
        else:
            print('Your Password is weak')

        if input('\nDo You want to continue?: ').lower() !='y':
            break

    print('Looks like You are good to go.')
    print('Do come by some other time. Ciao!')
if __name__ == '__main__':
    main()

