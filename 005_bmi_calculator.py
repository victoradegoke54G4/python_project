
class BMI:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def bmi_calc(self):
        try:
            bmi_calc = round((self.weight / (self.height **2)), 2)

        except ZeroDivisionError:
            print('Check Your Height Input')
        else:
            return bmi_calc
    

def get_float(prompt):
    '''Converts type to float with exception handling'''
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Invalid Input!')
            quit()


#user interface
def main():
    '''Allows User Interaction With Code'''

#user input
    print('Welcome to the Ultimate BMI Calculator.')

    userWeight = get_float('Enter your weight in kg: ')
    userHeight = get_float('Enter your height in m: ')

    person = BMI(userHeight, userWeight)
    bmi = person.bmi_calc()

    if userWeight > 0 and userHeight > 0: 
        
        if bmi < 18.5:
            print(f'Your BMI is {bmi} and you are underweight.')

        elif bmi < 25:
            print(f'Your BMI is {bmi} and you have a normal weight.')

        elif bmi < 30:
            print(f'Your BMI is {bmi} and you are overweight.')

        else:
            print(f'Your BMI is {bmi} and you are obesed.')

    else:
        print('Check your Input')
        quit()
main()