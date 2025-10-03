#greet user

print('Welcome To The Group Name Generator.')
while True:
    userName = input('What is your name?: ')
    if not userName:
        print('Check Your input!')
        continue
    else:
        print(f'Hello {userName}, welcome.\nLet\'s get you a group name. ')
    
    print( )
    
    #get parameters for generator
    favourite_color = input('What is your favourite colour?: ')
    favourite_animal = input('What is your favourite animal?: ')
    
    fav = favourite_animal and favourite_color
    if not fav or not isinstance(fav, str):
        print('Please, Check Input')
        print( )
        continue
    else:
    #show result
        print(f'Congratulations, {userName}! Your group name is {favourite_color + favourite_animal}.')
        break
# else: 
#     print('Thank You For Using The App.')