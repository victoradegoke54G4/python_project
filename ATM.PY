
# class atm:
#     def __init__(self, balance = 1000, pin = 1234):
#         self.balance = balance
#         self.pin = pin

#     def get_balance(self):
#         print("Your Balance is {}".format(self.balance))

#     def deposit_balance(self):
#         userDeposit_Input = int(input(print("Enter amount to deposit: ")))
#         depositedBalance = self.balance() + userDeposit_Input
#         if userDeposit_Input is True:
#             print("You have successfully deposited an amount of {} Naira. You now have a balance of {}".format(userDeposit_Input, depositedBalance))
#         else:
#             print("You have made a wrong Input")

#     def withdraw_balance(self):
#         userwithdraw_Input = int(input(print("Enter amount to withdraw: ")))
#         withdrawalBalance = self.balance() - userwithdraw_Input
#         if userwithdraw_Input is True:
#             print("You have successfully withdrawn an amount of {} Naira. You now have a balance of {}".format(userwithdraw_Input, withdrawalBalance))
#         else:
#             print("You have made a wrong Input")

#     def exit_program(self):
#         is_working = False

# def main(atm):
#     is_working = True

#     print("Welcome To The UBA ATM Simulator")
#     userPin_Input = int(input(print("Please, Enter your PIN: ")))
#     if userPin_Input != self.pin :
#         print("You have inputted the wrong Pin.")
#     else:
#         print("Main Menu: ")
#         print("1. Check Balance")
#         print("2. Deposit Balance")
#         print("3. Withdraw Balance")
#         print("4. Exit")
#         userChoice_Input = input(print("Enter Your Choice: "))

#         while is_working:

#             if userChoice_Input == 1:
#                 get_balance()

#             elif userChoice_Input == 2:
#                 deposit_balance()

#             elif userChoice_Input == 3:
#                 withdraw_balance()

#             elif userChoice_Input == 4:
#                 exit_program()

#             else:
#                 print("Wrong Input")

#         else:
#                 print("Thank You For Banking With Us.")

# main(atm)





# class ATM:
#     def __init__(self, balance=1000, pin=1234):
#         self.balance = balance
#         self.pin = pin

#     def get_balance(self):
#         print("Your Balance is {}".format(self.balance))

#     def deposit_balance(self):
#         userDeposit_Input = int(input("Enter amount to deposit: "))
#         if userDeposit_Input > 0:
#             self.balance += userDeposit_Input
#             print("You have successfully deposited {} Naira. New balance is {}".format(userDeposit_Input, self.balance))
#         else:
#             print("Invalid deposit amount.")

#     def withdraw_balance(self):
#         userwithdraw_Input = int(input("Enter amount to withdraw: "))
#         if 0 < userwithdraw_Input <= self.balance:
#             self.balance -= userwithdraw_Input
#             print("You have successfully withdrawn {} Naira. New balance is {}".format(userwithdraw_Input, s12elf.balance))
#         else:
#             print("Invalid or insufficient balance.")

# def main(atm):
#     print("Welcome To The UBA ATM Simulator")
#     userPin_Input = int(input("Please, Enter your PIN: "))
#     if userPin_Input != atm.pin:
#         print("Wrong Pin.")
#         return

#     is_working = True
#     while is_working:
#         print("\nMain Menu: ")
#         print("1. Check Balance")
#         print("2. Deposit Balance")
#         print("3. Withdraw Balance")
#         print("4. Exit")
#         userChoice_Input = int(input("Enter Your Choice: "))

#         if userChoice_Input == 1:
#             atm.get_balance()
#         elif userChoice_Input == 2:
#             atm.deposit_balance()
#         elif userChoice_Input == 3:
#             atm.withdraw_balance()
#         elif userChoice_Input == 4:
#             print("Thank You For Banking With Us.")
#             is_working = False
#         else:
#             print("Wrong Input")

# # Run program
# myATM = ATM()
# main(myATM)





class ATM:
    def __init__(self, balance=1000, pin=1234):
        self.balance = balance
        self.pin = pin

    def get_balance(self):
        print("Your Balance is {}".format(self.balance))

    def deposit_balance(self):
        userDeposit_Input = int(input("Enter amount to deposit: "))
        if userDeposit_Input > 0:
            self.balance += userDeposit_Input
            print("You have successfully deposited {} Naira. New balance is {}".format(userDeposit_Input, self.balance))
        else:
            print("Invalid deposit amount.")

    def withdraw_balance(self):
        userwithdraw_Input = int(input("Enter amount to withdraw: "))
        if 0 < userwithdraw_Input <= self.balance:
            self.balance -= userwithdraw_Input
            print("You have successfully withdrawn {} Naira. New balance is {}".format(userwithdraw_Input, self.balance))
        else:
            print("Invalid or insufficient balance.")

def main(atm):
    print("Welcome To The UBA ATM Simulator")

    # PIN retry system (3 attempts)
    attempts = 3
    while attempts > 0:
        userPin_Input = int(input("Please, Enter your PIN: "))
        if userPin_Input == atm.pin:
            break
        else:
            attempts -= 1
            print("Wrong PIN. You have {} attempt(s) left.".format(attempts))

    if attempts == 0:
        print("Too many wrong attempts. Card blocked.")
        return

    # If PIN is correct, show menu
    is_working = True
    while is_working:
        print("\nMain Menu: ")
        print("1. Check Balance")
        print("2. Deposit Balance")
        print("3. Withdraw Balance")
        print("4. Exit")
        userChoice_Input = int(input("Enter Your Choice: "))

        if userChoice_Input == 1:
            atm.get_balance()
        elif userChoice_Input == 2:
            atm.deposit_balance()
        elif userChoice_Input == 3:
            atm.withdraw_balance()
        elif userChoice_Input == 4:
            print("Thank You For Banking With Us.")
            is_working = False
        else:
            print("Wrong Input")

# Run program
myATM = ATM()
main(myATM)



# class atm:
#     def __init__(self, balance = 1000, pin = 1234):
#         self.balance = balance
#         self.pin = pin

#     def get_balance(self):
#         print("Your Balance is {}".format(self.balance))

#     def deposit_balance(self):
#         userDeposit_Input = int(input("Enter amount to deposit: "))
#         depositedBalance = self.balance + userDeposit_Input
#         if userDeposit_Input > 0:
#             self.balance = depositedBalance
#             print("You have successfully deposited an amount of {} Naira. You now have a balance of {}".format(userDeposit_Input, self.balance))
#         else:
#             print("You have made a wrong Input")

#     def withdraw_balance(self):
#         userwithdraw_Input = int(input("Enter amount to withdraw: "))
#         withdrawalBalance = self.balance - userwithdraw_Input
#         if userwithdraw_Input > 0 and withdrawalBalance >= 0:
#             self.balance = withdrawalBalance
#             print("You have successfully withdrawn an amount of {} Naira. You now have a balance of {}".format(userwithdraw_Input, self.balance))
#         elif withdrawalBalance < 0:
#              print("Insufficient balance. You cannot withdraw this amount.")
#         else:
#             print("You have made a wrong Input")

#     def exit_program(self):
#         print("Thank You For Banking With Us.")


# def main():
#     is_working = True

#     print("Welcome To The UBA ATM Simulator")
#     atm_instance = atm() # Create an instance of the atm class
#     userPin_Input = int(input("Please, Enter your PIN: "))

#     if userPin_Input != atm_instance.pin :
#         print("You have inputted the wrong Pin.")
#     else:
#         print("Main Menu: ")
#         print("1. Check Balance")
#         print("2. Deposit Balance")
#         print("3. Withdraw Balance")
#         print("4. Exit")

#         while is_working:
#             userChoice_Input = input("Enter Your Choice: ")

#             if userChoice_Input == '1':
#                 atm_instance.get_balance()

#             elif userChoice_Input == '2':
#                 atm_instance.deposit_balance()

#             elif userChoice_Input == '3':
#                 atm_instance.withdraw_balance()

#             elif userChoice_Input == '4':
#                 is_working = False
#                 atm_instance.exit_program()

#             else:
#                 print("Wrong Input")

# main()