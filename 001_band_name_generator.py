#greet user
print('Welcome To The Group Name Generator.')
userName = input(' What is your name?: ')
print(f'Hello {userName}, welcome.\nLet\'s get you a group name. ')

#get parameters for generator
favourite_color = input('What is your favourite colour?: ')
favourite_animal = input('What is your favourite animal?: ')

#show result
print(f'Congratulations, {userName}! Your group name is {favourite_color} {favourite_animal}.')