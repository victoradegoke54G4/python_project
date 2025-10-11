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

for row in range(3):  
      for column in range(5):
            column +=1
            print(column, end = ' ')
      print()
# ''' for every row in range 3 (0,1,2) each row number 0 would be substituted with 1 2 3 from column vice versa for num of rows 2,3'''

# for row in range(3):
#     print('1'+' '+'2'+' '+ '3')


# print('ab', end=' ')
# print('bc')
