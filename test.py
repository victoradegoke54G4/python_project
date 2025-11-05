# def func(x):
#     try:
#         if x // 0 == 1 :
#             return 1
#         else: return'dopemu'
#     except ArithmeticError:
#         raise 'opsie'

# # print(func(0))

# data = ['abc', 'def', 'abcde','efg']
# print(max(data))

# data1 = [1,2,3,8,4,5,9]
# print(max(data1))

# x = float('23.42')
# print(bool(x) + True)

# def factorial(n):
#     fact = 1
#     for num in range (2, n + 1):
#         fact *= num 
#         print(num)
#     return fact

# print(factorial (5))

# fact = 1
# for num in range(3):
#     for num in range (3):
#         fact = fact * num
#         print(fact, end=' ')
    
#     print(fact)

""""".................................................."""
# space_counter = ''
# def right_justify():
#     global space_counter
#     space_counter += ' '

# mana = {space_counter} + 'Allen'
# [right_justify() for x in range (70) ]
# # mana = space_counter + 'Allen'
# print(mana)

# counter = 3
# def update_counter():
#     global counter
#     counter +=1
#     return counter

# [update_counter() for x in range(10)]
# print(update_counter())

# counter = 0
# dot_counter = ''
# def update_counter():
#     global counter
#     counter += 1
#     global dot_counter
#     dot_counter += '.'

# [update_counter() for x in range (40) ]
# print(counter)
# print(dot_counter)

""""".................................................."""

# def display_info(number_of_updates = 1):
#     counter = 100
#     dot_counter = ''

#     def update_counter():
#         nonlocal counter, dot_counter
#         counter += 1
#         dot_counter += '.'
    
#     [update_counter() for _ in range (number_of_updates)]
#     print(counter)
#     print(dot_counter)

# display_info(10)


""""".................................................."""

# x = 1

# print(x != 1)


""""".................................................."""
# list1 = [12, 15, 32, 40, 52, 75, 122, 150, 100, 200]

# def number_divisible_by_five(p_list1):
     
#     for item in p_list1: 
#        if item >130:
#            break
#        if item % 5 == 0:
#            print(item)
#     print('STOP')

# number_divisible_by_five(list1)


# """" TEMPERATURE CHECKER"""""

# def get_float(prompt):
#     try:
#         return float(input(prompt))
    
#     except (ValueError, TypeError):
#         print('Invalid Input')

# def temperatureCalc(p_temp_input):
#     '''Calculates the condition for execution'''
#     if p_temp_input > 28 :
#         return 'Hot'
#     elif 18 < p_temp_input > 28 :
#         return 'Warm'
#     else:
#         return 'Cold'
    
# def main():
#     '''Collects User's Input'''
#     userTemperatureInput = get_float('Enter Temperature Value: ')
#     temperatureCalc(userTemperatureInput)
    
# main()

"""" MAX INPUT NUMBERS"""""

# def get_float(prompt):
#     try:
#         return float(input(prompt))
    
#     except (ValueError, TypeError):
#         print('Invalid Input')

# def max_logic(p_first_name, p_second_name, p_third_name):
#     if p_first_name > p_second_name:
#         if p_first_name > p_third_name:
#             return p_first_name
#         else:
#             return p_third_name
#     else:
#         if p_second_name > p_third_name:
#             return p_second_name
#         else:
#             return p_third_name
              
# def main():
#     first_number = get_float('Enter First Number: ')
#     second_number = get_float('Enter Second Number: ')
#     third_number = get_float('Enter Third Number: ')

#     print(max_logic(first_number,second_number,third_number))

# main()   

# ❌

"""" SIMULTANEOUS COUNT, SUM AND AVERAGE OF INPUT NUMBERS"""""

# def main():
#     count = 0
#     num = 0
#     while True:
#         userInput = input('Enter a number: ').lower()
#         if userInput == 'done':
#             break
#         else:
#             count +=1
#             main_input = float(userInput)
#             num += main_input

#     print(f'The count is {count}')
#     print(f'Sum is : {num}')
#     print('Average is {}'.format(num/count))

# main()




# alphabet = ('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z').split(',')
# for alphabet in alphabet[::-1]:
# print(alphabet)
# message = 'c','b'
# shift = 1

# cipher = ''
# for char in  message:
#     position= alphabet.index(char)
#     new_position = position + shift
#     new_char = alphabet[new_position]
#     cipher +=new_char
# print('The encrypted message is {}. '. format(cipher))


#     print(alphabet)




# class SafeInput:
#     @staticmethod
#     def get_int(prompt, min_val=None, max_val=None):
#         while True:
#             try:
#                 val = int(input(prompt))
#                 if (min_val and val < min_val) or (max_val and val > max_val):
#                     print(f"Enter a number between {min_val} and {max_val}.")
#                     continue
#                 return val
#             except ValueError:
#                 print("Enter a valid integer.")

#     @staticmethod
#     def get_choice(prompt, options):
#         while True:
#             val = input(prompt).strip().lower()
#             if val in [str(o).lower() for o in options]:
#                 return val
#             print(f"Choose from: {', '.join(map(str, options))}")
# SafeInput()

# def safe_yes_no(prompt):
#     while True:
#         choice = input(prompt + " (y/n): ").strip().lower()
#         if choice in ['y', 'yes']:
#             return True
#         elif choice in ['n', 'no']:
#             return False
#         print("❌ Please enter 'y' or 'n'.")



# def safe_number(prompt, number_type=int, min_val=None, max_val=None):
#     while True:
#         try:
#             value = number_type(input(prompt))
#             if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
#                 print(f"Enter a number between {min_val} and {max_val}.")
#                 continue
#             return value
#         except ValueError:
#             print("❌ Please enter a valid {}.".format(number_type.__name__))



# def safe_choice(prompt,options):
#     while True:
#         choice = input(prompt).strip().lower()
      # for option in options:                                      # if choice in [str(opt).lower() for opt in options]:
#             if choice in str(option).lower().strip():
#                 return choice
#         print(f'Invalid Choice.{', '.join(map(str,options))}')

# while True:
#       d =safe_yes_no('> ')
#       if d:
#           continue
#       else:
#           print('ttttt')
#           break
#       # print(safe_yes_no('> '))


# d =[0,1,2,3]
# e =[0,1,2,3]
# for ds in d:
#       for es in e:
#             es+=1
#             print(es, end = ' ')

#       print()

# d= [es for es in range(4)]
# print(d)

# for row in range(3):  
#       for column in range(5):
#             column +=1
#             print(column, end = ' ')
#       print()

# message = ['123test123', '9045', 'john', 'raymonD', 'ahmad']
# vowels = ('a','e','i','o','u')


# piglatin = []
# for word in message:
#     prefix = ''
#     suffix = ''
#     while len(word) > 0 and not word[0].isalpha():
#         prefix += word[0]
#         word = word[1:]

#     while len(word) > 0 and not word[-1].isalpha():
#         suffix += word[-1]
#         word = word[:-1]

#     if len(word) > 0:
#         piglatin.append(word)
    
#     if not word:
#         continue
#     was_upper = word.isupper()
#     was_title = word.istitle()

#     if word[0] in vowels:
#             word = word + 'yay'

#     else:
#         while len(word) > 0 and word[0] not in vowels:
#             word = word[1:] + word[0] + 'ay'
    

#     if was_upper:
#         word.upper()
#     elif was_title:
#         word.title()
    
#     combined_letters = prefix + word + suffix
    
#     print(combined_letters)

# import random

# d = random.randint(0,2)
# print(d)

# number_list = list(range(70))
# print(number_list)

# import random


# g = random.randint(0,5)
# print(g)
# lotteryNumbers = [1,2,3,4,5]

# ''' for every row in range 3 (0,1,2) each row number 0 would be substituted with 1 2 3 from column vice versa for num of rows 2,3'''

# for row in range(3):
#     print('1'+' '+'2'+' '+ '3')


# print('ab', end=' ')
# print('bc')

# import random
# from words import word_list
# import logo_stages

# def main():
#     print(logo_stages.logo)
#     blanks = []

#     while True:
#         random_word = random.choice(word_list)
#         for letters in random_word:
#             blanks.append('_')

#         chances = len(logo_stages.hangman_stages)-1
#         print(logo_stages.hangman_stages[chances])
#         print(blanks)
#         guessedletters = []
#         correctguesses = []
#         while chances > 0:
#             userGuess = input('\nGuess The Word: ').upper()
#             if userGuess in guessedletters:
#                 print('You already made that guess.')
#                 chances-=1
#                 print(logo_stages.hangman_stages[chances])
#                 print(blanks)
#                 continue
#             else:
#                 guessedletters.append(userGuess)
#                 if not userGuess or userGuess not in random_word.strip():
#                     chances-=1
#                     print(logo_stages.hangman_stages[chances])
#                     # if chances == 0:
#                     #     print('Game Over!! You ran Out of Life.')
#                 else:
#                     correctguesses.append(userGuess)
#                     guessedWordsIndex = random_word.index(userGuess)
#                     blanks[guessedWordsIndex] = userGuess
#                 print(blanks)

#         if len(correctguesses) == random_word:
#             print('Congratulations! You guessed correct.')
#         else:
#             print('\nThe word is {}.'.format(random_word))
#             if chances == 0:
#                 print('\nGame Over!! You ran Out of Life.')

#         print()
#         replayquestion = input('Would you like to play once again?(y/n) ').upper()
#         if replayquestion == 'N':
#             break

#     print('Thank You for Playing.')
# main()


#####
# import random

# userNumber_list = []
        

# def get_int(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#             return value
            
#         except (ValueError, TypeError):
#             print('Invalid Input')

# def getCostOfPlays(numberOfPlays):
#     cost = 2 * numberOfPlays
#     return f'${cost}'

# def getLotteryNumbers():
#         lotteryNumbers = list(range(1,70))
#         random.shuffle(lotteryNumbers)
#         mainlotteryNumbers = lotteryNumbers[0:5]
#         powerballNumber = random.randint(0,26)        
#         return mainlotteryNumbers, powerballNumber


# def main():
#     # ask user for five numbers
#     while True:
#         print('Enter 5 different numbers frome 1 to 69, with spaces between each number. (For example: 5 12 27 30)')
#         user_input = '> '
#         userNumber = input(user_input)
        
#         try:
#             number_list = userNumber.split()
#             if len(number_list) != 5:
#                 print('Enter five digits with spaces in between.')
#                 continue

#             for i in range(5):
#                 number_list[i] = int(number_list[i])

#             for numbers in number_list:
#                 if not (1 <= numbers <= 69):
#                     print('Please enter numbers between 1 and 69.') 
#                     break
#             if len(set(number_list)) != 5:
#                 print('Enter five different numbers')
#                 continue

#         except (ValueError, TypeError):
#             print('Invalid Input') 

#         except AttributeError:
#             print('Enter numbers with spaces in between')
#         break
    
#     #ask user for powerball number
#     while True:
#         print('Enter the powerball number from 1 to 26')
#         userP_input = '> '
#         userPNumber = get_int(userP_input)
#         if not (1 <= userPNumber <= 26):
#             print('Please enter numbers between 1 and 26.') 
#             continue
#         break

#     #ask user plays
#     while True:
#         print('How many times would you love to play?(Max: 1000000): ')
#         user_input = '> '
#         numberOfPlays = get_int(user_input)
#         if not (1 <= numberOfPlays <= 1000000):
#                 print('Please enter numbers between 1 and 1000000.') 
#                 continue
#         break

#     #running the simulation
#     print(f'It costs {getCostOfPlays(numberOfPlays)} to play {numberOfPlays} times, but don\'t worry, I\'m sure you\'ll win it all back.')
#     input('Press any key to start game.')
#     for num in range(numberOfPlays):
#         lotteryNumbers, powerballNumber = getLotteryNumbers()
#         print('The winning numbers are: ', end='')
#         allwinningNumbers = ''
#         for num in lotteryNumbers:
#             allwinningNumbers += str(num) + ' '
#         allwinningNumbers += ' and ' + str(powerballNumber)+'.'
#         print(allwinningNumbers)
#         if ((set(lotteryNumbers) == set(userNumber_list)) and (powerballNumber == userPNumber)):
#             print( )
#             print('Congratulations! You have won the powerball lottery.')
#             break
#     print('You lost!')
#     print(f'You have successfully wasted {getCostOfPlays(numberOfPlays)}')
        
# main()


###
# from turtle import clear
# from art import logo
# from quiz_question import quiz


# def get_player(prompt):
#     while True:
#         try:
#             value = input(prompt).strip()
#             if not value: 
#                 print('Check Input')
#                 continue
#             return value
#         except (ValueError,TypeError):
#             print('Please enter valid Input')

# def check_answer(question_num, answer, attempts, player):
#     clear()
#     correct_answer = quiz[question_num]['answer']
#     if correct_answer.lower() == answer.lower():
#         print(f'Correct Answer! \n{player}\'s score is {score_dict[player] + 1}')
#         return True
#     print(f'Wrong Answer! \nYou have {attempts-1} attempts left! \nTry Again.')
#     return False

# def switch_users(p_user_index):
#     if p_user_index == 0:
#         return 1
#     return 0

# def check_winner(player1,player2):
#     if player1 > player2:
#         print(f'{player1} won the quiz with {score_dict[player1]}')
#     elif player1 < player2:
#         print(f'{player2} won the quiz with {score_dict[player2]}')
#     else:
#         print('It is a draw.')
    
# def main():
#     print(logo)

#     print('There are a total of 6 questions you can skip any question at anytime by pressing \'skip\'.')
#     input('Press any key to continue... ')
#     players = get_player('Enter 2 players name with space: ')
#     player_list = players.split(' ')
#     score_dict = dict.fromkeys(player_list, 0)
#     current_player = player_list[0]
#     attempts = 2
#     for questions in quiz:
#         print('...................................')
#         print(f'It is {current_player}\'s turn')
#         while attempts > 0:
#             print(quiz[questions]['question'])
#             userAnswer = input('Enter answer.[To move to the next question, press \'skip\'.]: ').lower()
#             if userAnswer == 'skip':
#                 break
#             check = check_answer(questions,userAnswer,attempts, current_player)
#             if check:
#                 score_dict[current_player] += 1
#                 break
#             attempts-=1

#         current_playerIndex = player_list.index(current_player)
#         next_player_index = switch_users(current_playerIndex)
#         current_player = current_player[next_player_index]

#     check_winner(score_dict[player_list[0]], score_dict[player_list[1]])

#     input('Do you want to see the answers?: ').lower()
#     if input() == 'y':
#         # for questions in quiz:
#         #     print(f'{quiz}')
        

# if __name__ == '__main__':
#     main()

# print(help())



# import os
# from art import logo
# from quiz_question import quiz

# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def get_player(prompt):
#     while True:
#         try:
#             value = input(prompt).strip()
#             if not value:
#                 print('Check Input')
#                 continue
#             return value
#         except (ValueError, TypeError):
#             print('Please enter valid Input')

# def check_answer(question_num, answer, attempts, player, score_dict):
#     clear()
#     correct_answer = quiz[question_num]['answer']
#     if correct_answer.lower() == answer.lower():
#         print(f'Correct Answer! \n{player}\'s score is {score_dict[player] + 1}')
#         return True
#     print(f'Wrong Answer! \nYou have {attempts - 1} attempts left! \nTry Again.')
#     return False

# def switch_users(p_user_index):
#     return 1 if p_user_index == 0 else 0

# def check_winner(p1_name, p1_score, p2_name, p2_score):
#     if p1_score > p2_score:
#         print(f'{p1_name} won the quiz with {p1_score} points!')
#     elif p2_score > p1_score:
#         print(f'{p2_name} won the quiz with {p2_score} points!')
#     else:
#         print('It is a draw!')

# def main():
#     print(logo)
#     print('There are a total of 6 questions. You can skip any question at any time by typing "skip".')
#     input('Press any key to continue... ')
    
#     players = get_player('Enter 2 players name separated by space: ')
#     player_list = players.split(' ')
#     score_dict = dict.fromkeys(player_list, 0)
#     current_player = player_list[0]
#     attempts = 2

#     for questions in quiz:
#         print('-----------------------------------')
#         print(f'It is {current_player}\'s turn')
#         while attempts > 0:
#             print(quiz[questions]['question'])
#             userAnswer = input('Enter answer [or "skip" to move on]: ').lower()
#             if userAnswer == 'skip':
#                 break
#             check = check_answer(questions, userAnswer, attempts, current_player, score_dict)
#             if check:
#                 score_dict[current_player] += 1
#                 break
#             attempts -= 1

#         current_player_index = player_list.index(current_player)
#         next_player_index = switch_users(current_player_index)
#         current_player = player_list[next_player_index]

#     check_winner(player_list[0], score_dict[player_list[0]], player_list[1], score_dict[player_list[1]])

#     see_answers = input('Do you want to see the answers? (y/n): ').lower()
#     if see_answers == 'y':
#         for key, value in quiz.items():
#             print(f"{value['question']} → {value['answer']}")

# if __name__ == '__main__':
#     main()

#####



# class EmployeeDetails:

#       def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#       # def __get_salary(self):
#       #     return self.__salary
      
#       # def __set_salary(self, new_salary):
#       #       self.__salary = new_salary
      
#       # salary = property(__get_salary, __set_salary)

#       @property
#       def salary(self):
#           return self.__salary
      
#       @salary.setter
#       def salary(self, new_salary):
#           self.__salary = new_salary

# employee1 = EmployeeDetails('Dan', 100)
# employee2 = EmployeeDetails('John', 500)
# print()
# print(employee1.name)
# print(employee1.salary)
# employee1.salary = 300
# print(employee1.salary)
# employee1.set_salary(300)
# print(employee1.get_salary())
    

def process_arr(arr, i=0):
    if i == len(arr): return process(arr[i])
    process_arr(arr, i+1)



