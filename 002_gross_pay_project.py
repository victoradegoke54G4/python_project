#Calculate user's pay with estimated figure.

def usercalc(userWorkingrate, userWorkinghours):
    userPay = userWorkingrate * userWorkinghours
    return userPay

#userinterface
def main():
    print('Welcome to the Gross Pay App')
    userWorkinghours = float(input('Enter your working hours: '))
    userWorkingrate = float(input('Enter your working rate per hour: '))
    userPay = usercalc(userWorkingrate, userWorkinghours)
    print(f'Your pay is ${round(userPay, 2)}')

main()