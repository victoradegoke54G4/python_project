# Calculate user's pay with estimated figure.


def usercalc(userWorkingrate, userWorkinghours):
    if userWorkinghours < 40:
        userPay = userWorkingrate * userWorkinghours
        return userPay
    else:
        overtime = userWorkinghours - 40
        userPay = (40 * userWorkingrate) + (overtime * userWorkingrate * 1.5)
        return userPay


# userinterface


def main():
    print("Welcome to the Gross Pay App")
    try:
        userWorkinghours = float(input("Enter your working hours: "))
        userWorkingrate = float(input("Enter your working rate per hour: "))
    except ValueError:
        print("Please check Input.")
    else:
        userPay = usercalc(userWorkingrate, userWorkinghours)
        print(f"Your pay is ${round(userPay, 2)}")


main()
