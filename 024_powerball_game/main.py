import random
from ascii_art import logo

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except (ValueError, TypeError):
            print('Invalid input. Please enter a number.')

def getCostOfPlays(numberOfPlays):
    cost = 2 * numberOfPlays
    return f'${cost}'

def getLotteryNumbers():
    lotteryNumbers = list(range(1, 70))
    random.shuffle(lotteryNumbers)
    mainlotteryNumbers = lotteryNumbers[:5]
    powerballNumber = random.randint(1, 26)
    return mainlotteryNumbers, powerballNumber

def main():
    print(logo)
    print('Welcome to the Powerball Lottery Simulator!\n')

    # Ask for user’s 5 main numbers
    while True:
        user_input = input('Enter 5 different numbers from 1 to 69 (e.g., 5 12 27 30 59): ')
        try:
            number_list = [int(num) for num in user_input.split()]
            if len(number_list) != 5:
                print('Please enter exactly 5 numbers.')
                continue
            if any(num < 1 or num > 69 for num in number_list):
                print('Numbers must be between 1 and 69.')
                continue
            if len(set(number_list)) != 5:
                print('Please enter 5 different numbers.')
                continue
            userNumber_list = number_list
            break
        except ValueError:
            print('Invalid input. Please enter numbers only.')

    # Ask for Powerball number
    while True:
        userPNumber = get_int('Enter the Powerball number (1 to 26): ')
        if not (1 <= userPNumber <= 26):
            print('Please enter a number between 1 and 26.')
            continue
        break
  
    # Ask number of plays
    while True:
        numberOfPlays = get_int('How many times would you like to play? (1 to 1,000,000): ')
        if not (1 <= numberOfPlays <= 1000000):
            print('Enter a valid number of plays between 1 and 1,000,000.')
            continue
        break

    # Run simulation
    print(f"\nIt costs {getCostOfPlays(numberOfPlays)} to play {numberOfPlays} times. Let's see if you win...")
    input('Press ENTER to start.\n')

    won = False
    for num in range(numberOfPlays):
        lotteryNumbers, powerballNumber = getLotteryNumbers()
        print('Winning numbers:', ' '.join(map(str, lotteryNumbers)), f'and {powerballNumber}')

        if set(lotteryNumbers) == set(userNumber_list) and powerballNumber == userPNumber:
            print("\n🎉 Congratulations! You’ve won the Powerball lottery! 🎉")
            won = True
            break

    if not won:
        print('\nYou lost!')
        print(f'You’ve successfully wasted {getCostOfPlays(numberOfPlays)} 😅')

if __name__ == '__main__':
    main()
