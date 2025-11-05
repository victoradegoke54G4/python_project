import mapcode
import random

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
        vertical, horizontal  = random.randint(0,2), random.randint(0,2)
        mapcode.map1[horizontal][vertical] = '$$'
        return f'{horizontal+1}{vertical+1}'
    
    def userChoice(self): 
        try:
            horizontalp, verticalp = int(self.position[0]), int(self.position[1])
            mapcode.map1[horizontalp-1][verticalp-1] = 'k'
        except (IndexError, ValueError):
            print('\nYour Choice Is Not Valid')


def main():
    print("Welcome to Find the Golden Star Game 🌟")
    goldenstarposition = FindGoldenStar.computerChoice()   # generate once

    while True:
        user_input = FindGoldenStar.get_choice('\nEnter Map Coordinates: ')
        fgs = FindGoldenStar(user_input)
        fgs.userChoice()
        mapcode.print_map(mapcode.map1)

        if goldenstarposition == user_input:
            print('\n🎉 Congratulations! You have found the Golden Star!')
            break
        else:
            print('\nOops, You couldn\'t find it. Try again!')


if __name__ == '__main__':
    main()
