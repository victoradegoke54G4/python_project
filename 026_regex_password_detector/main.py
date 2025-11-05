def main():
    """Display user Interface"""
    print('='*20)
    print('Let\'s Check Your Password\'s strength.')
    print('Type Q to quit')
    while True:
        user_input = input('\nEnter Your Password: ')
        if user_input == 'Q':
            break

        if user_input:
            print('yam')
            break

        else:
            print('You need to make an Input.')

    print('Looks like You are good to go.')
    print('Do come by some other time. Ciao!')
if __name__ == '__main__':
    main()