

import os
from art import logo
from quiz_question import quiz

def clear():
    """Clears the terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_player(prompt):
    """Gets player names with validation."""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print('Check Input')
                continue
            return value
        except (ValueError, TypeError):
            print('Please enter valid Input')


def check_answer(question_num, answer, attempts, player, score_dict):
    """Checks if the player's answer is correct and updates score."""
    clear()
    correct_answer = quiz[question_num]['answer']
    if correct_answer.lower() == answer.lower():
        print(f'Correct Answer!\n{player}\'s score is {score_dict[player] + 1}')
        return True
    print(f'Wrong Answer!\nYou have {attempts - 1} attempts left!\nTry Again.')
    return False


def switch_users(p_user_index):
    """Switches turns between players."""
    return 1 if p_user_index == 0 else 0


def check_winner(p1_name, p1_score, p2_name, p2_score):
    """Determines and prints the winner of the quiz."""
    print('\n===== FINAL RESULTS =====')
    if p1_score > p2_score:
        print(f'{p1_name} won the quiz with {p1_score} points!')
    elif p2_score > p1_score:
        print(f'{p2_name} won the quiz with {p2_score} points!')
    else:
        print('It is a draw!')


def main():
    """Main function to run the quiz game."""
    print(logo)
    print('There are a total of 6 questions. You can skip any question at any time by typing "skip".')
    input('Press any key to continue... ')

    # Player setup
    players = get_player('Enter 2 players name separated by space: ')
    player_list = players.split(' ')
    score_dict = dict.fromkeys(player_list, 0)
    current_player = player_list[0]
    attempts = 2

    # Quiz loop
    for questions in quiz:
        print('-----------------------------------')
        print(f'It is {current_player}\'s turn')
        attempts = 2  # Reset attempts per question

        while attempts > 0:
            print(quiz[questions]['question'])
            userAnswer = input('Enter answer [or "skip" to move on]: ').lower().strip()

            if not userAnswer:
                print('Please enter something. You cannot leave it blank.')
                continue
            if userAnswer == 'skip':
                break

            check = check_answer(questions, userAnswer, attempts, current_player, score_dict)
            if check:
                score_dict[current_player] += 1
                break
            attempts -= 1

        # Switch player turn
        current_player_index = player_list.index(current_player)
        next_player_index = switch_users(current_player_index)
        current_player = player_list[next_player_index]

    # Display winner
    check_winner(player_list[0], score_dict[player_list[0]], player_list[1], score_dict[player_list[1]])

    # Option to show answers
    see_answers = input('\nDo you want to see the answers? (y/n): ').lower()
    if see_answers == 'y':
        print('\n===== QUIZ ANSWERS =====')
        for key, value in quiz.items():
            print(f"{value['question']} → {value['answer']}")

    print('\nThank you for playing the quiz!')


if __name__ == '__main__':
    main()
