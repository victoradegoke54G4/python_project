import random
import mapcode 

class FindGoldenStar:
    def __init__(self, position):
        self.position = position

    @staticmethod
    def get_choice(prompt):
        while True:
            value = (input(prompt)).strip()
            if value and len(value) == 2 and value.isdigit():
                return value
            print('Invalid Input. Enter two digits (e.g., 11, 23)')

    @staticmethod
    def computerChoice():
        """Randomly hide the golden star and return its position as a string like '23'"""
        vertical, horizontal = random.randint(0, 2), random.randint(0, 2)
        mapcode.map1[horizontal][vertical] = '🌟'
        return f'{horizontal + 1}{vertical + 1}'

    def userChoice(self):
        """Mark the user's chosen cell on the map"""
        try:
            horizontalp, verticalp = int(self.position[0]), int(self.position[1])
            mapcode.map1[horizontalp - 1][verticalp - 1] = '🌠'
        except (IndexError, ValueError):
            print('\nYour Choice Is Not Valid')


def reset_map():
    """Reset the 3x3 map for a new round"""
    mapcode.map1 = [['⬜', '⬜', '⬜'],
                    ['⬜', '⬜', '⬜'],
                    ['⬜', '⬜', '⬜']]


def main():
    print(" Welcome to the Find the Golden Star Game ")

    while True:
        reset_map()
        golden_star_position = FindGoldenStar.computerChoice()
        user_input = FindGoldenStar.get_choice('\nEnter Map Coordinates: ')
        fgs = FindGoldenStar(user_input)
        fgs.userChoice()
        mapcode.print_map(mapcode.map1)

        if golden_star_position == user_input:
            print('\n🎉 Congratulations! You found the Golden Star!')
        else:
            print('\n❌ Oops! You missed the Golden Star.')

        # ask user to play again or quit
        play_again = input('\nWould you like to play again? (Y/N): ').lower()
        if play_again != 'y':
            print('\nThanks for playing! See you next time ')
            break


if __name__ == '__main__':
    main()
