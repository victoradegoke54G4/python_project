

class TemperatureConverter:
    
    @staticmethod
    def to_fahrenheit(c):
       result = (c * 9/5) + 32
       return result
        
    @staticmethod
    def to_celsius(f):
        result = (f - 32) * 5/9
        return result 


def get_choice(prompt, options):
    ''' Keeps asking until user enters valid choice.'''
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        else:
            print(f'Invalid Choice!. Options: {' , '.join(options)}')
                  

def get_float(prompt):
    '''Converts type to float with exception handling'''
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Input Correct Value.')
            # quit()b
        except TypeError:   
            print('Check Type Input.')
            # quit()

#user's interface
def main(): 
    '''Allows User Interaction With Code'''

    isworking = True
    while isworking:
        print('Welcome To The Ultimate Temperature Conversion App')
        conversion_choice = get_choice('What would you like to convert to? C or F: ', ['c', 'f'])

        if conversion_choice == 'c':
            conversioninputCelsius = get_float('Enter Fahrenheit Value for Conversion: ')
            print(f'Your result from {conversioninputCelsius} Fahrenheit is {TemperatureConverter.to_celsius(conversioninputCelsius):.2f} Celsius')
            isworking = False

        elif conversion_choice == 'f':
            conversioninputFahrenheit = get_float('Enter Celsius Value for Conversion: ')
            print(f'Your result from {conversioninputFahrenheit} Celsius is {TemperatureConverter.to_fahrenheit(conversioninputFahrenheit):.2f} Fahrenheit')
            isworking = False
        else:
            print('Invalid Input. Try again.')
       
    else:
        print('Thank You For Using The App.')

main()