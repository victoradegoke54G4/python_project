import os 
import random
from words import word_list
import logo_stages

def clear():
    """Clears the terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print(logo_stages.logo)

    while True:
        random_word = random.choice(word_list).upper()
        blanks = ['_'] * len(random_word)
        guessedletters = []
        chances = len(logo_stages.hangman_stages) - 1

        print(logo_stages.hangman_stages[chances])
        print(' '.join(blanks))

        while chances > 0:
            userGuess = input('\nGuess a letter: ').upper().strip()
            clear()
            if not userGuess.isalpha() or len(userGuess) != 1:
                print("Enter a single valid letter.")
                continue

            if userGuess in guessedletters:
                print('You already made that guess.')
                continue

            guessedletters.append(userGuess)

            if userGuess not in random_word:
                chances -= 1
                print(f"\nWrong guess! You have {chances} chances left.")
                print(logo_stages.hangman_stages[chances])
            else:
                for i in range(len(random_word)):
                    if random_word[i] == userGuess:
                        blanks[i] = userGuess

            print(' '.join(blanks))

            if '_' not in blanks:
                print('\n🎉 Congratulations! You guessed the word:', random_word)
                break

            if chances == 0:
                print(f'\n💀 Game Over! The word was {random_word}')

        replayquestion = input('\nWould you like to play again? (y/n): ').upper()
        if replayquestion == 'N':
            print('\nThank you for playing!')
            break

if __name__ == '__main__':
    main()
