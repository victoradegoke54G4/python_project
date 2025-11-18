#Calculate total price of dict.items() while manipulating dictionary



def get_choice(prompt, options):
    ''' Keeps asking until user enters valid choice.'''
    while True:
        choice = input(prompt).lower()
        if choice in [str(option).lower().strip() for option in options]:
            return choice
        else:
            print(f"Invalid Choice!. Options: {' , '.join(map(str,options))}")


class ShoppingCart:

    def __init__(self):
        self.available_parts = ('computer, monitor, keyboard, mouse, hdmi cable, dvd drive, quit program').upper().strip().split(',')
        self.price_quantity = {

            'computer': {'price': 500, 'quantity': 10},
            'monitor': {'price': 200, 'quantity': 8},
            'keyboard': {'price': 500, 'quantity': 5},
            'mouse': {'price': 10, 'quantity': 0},
            'hdmi cable': {'price': 20, 'quantity': 7},
            'dvd drive': {'price': 50, 'quantity': 5}

        }
        
    def get_total(self, p_choice):
        total_price = 0 
        # global total_price
        for choice in p_choice:
            if not choice.isdigit():
                print('Invalid Choice.')
                continue
            chosenItem = self.available_parts[int(choice)-1].lower().strip()
            # if chosenItem == "quit program":
            #     continue
            if self.price_quantity[chosenItem]['quantity'] <=0:
                print('Sorry, The item is out of stock'.title())
                continue
            else:
                print(f'Adding {chosenItem.title()} Item To Cart'.title())
                self.price_quantity[chosenItem]['quantity'] -=1
                total_price +=  self.price_quantity[chosenItem.strip()]['price']
        return total_price
                

    

def main():
    '''allows user to interact with program'''
    cart = ShoppingCart()
    print('\n==== WELCOME TO WALMART ====')
    print('> ADD ITEMS TO YOUR CART\n')

    for index, parts in enumerate(cart.available_parts, 1):
        print('{}.{}'.format(str(index),parts.upper().strip()))
        
    chosen_list = []
    while True:
        userInput = get_choice('\nWhat would you like to add to your cart?: '.title(), ['1','2','3','4','5','6','7'])
        chosen_list.append(userInput)
        if not userInput == '7':
            total = cart.get_total(chosen_list)
        else:
            break
    if total == 0:
        print('\nYou did not make any purchase.'.title())
    else:
        print('\nThe Total price is : {}'.title().format(total))
    print('\nThank You For Shopping With Us. Have A Great Day!')

if __name__ == '__main__':
    main() 