import random


def main():
    while True:
        Dice1 = random.randint(1, 6)
        print(f"Dice1 : {Dice1}")
        Dice2 = random.randint(1, 6)
        print(f"Dice2 : {Dice2}")

        choice = input("Do You Want To Continue (y/n): ").lower()
        if not choice:
            print("Invalid Input!")
            if choice == "n":
                break
            else:
                continue

    print("Thank You For Using The App!")


main()
