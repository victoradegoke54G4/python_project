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

