
class TemperatureConverter:
    
    @staticmethod
    def to_fahrenheit(c):
       result = (c * 9/5) + 32
       return result
        
    @staticmethod
    def to_celsius(f):
        result = (f - 32) * 5/9
        return result 

#user's interface
def main(): 
    isworking = True
    while isworking:
        print('Welcome To The Ultimate Temperature Conversion App')
        conversion_choice = input('What would you like to convert to? C or F: ').lower()

        if conversion_choice == 'c':
            conversioninputCelsius = float(input('Enter Fahrenheit Value for Conversion: '))
            print(f'Your result from {conversioninputCelsius} Fahrenheit is {TemperatureConverter.to_celsius(conversioninputCelsius):.2f} Celsius')
            isworking = False
        elif conversion_choice == 'f':
            conversioninputFahrenheit = float(input('Enter Celsius Value for Conversion: '))
            print(f'Your result from {conversioninputFahrenheit} Celsius is {TemperatureConverter.to_fahrenheit(conversioninputFahrenheit):.2f} Fahrenheit')
            isworking = False
        else:
            print('Invalid Input. Try again.')
    else:
        print('Thank You For Using The App.')

main()