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
#     print(counter)

# update_counter()

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
