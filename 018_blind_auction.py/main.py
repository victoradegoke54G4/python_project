from ascii_art import logo

class BlindAuction:
    def __init__(self):
        self.bidderdetails = {}

    @staticmethod
    def get_name(prompt):
        while True:
            name = input(prompt).lower().strip()
            if not name or name.isdigit():
                print("Input only alphabets.")
                continue
            else:
                return name

    @staticmethod
    def get_int(prompt):
        while True:
            try:
                amount = int(input(prompt))
                return amount
            except (ValueError, TypeError):
                print("Invalid Input.")

    @staticmethod
    def get_yes_no(prompt):
        while True:
            choice = input(prompt + '(y/n) :').lower().strip()
            if choice in ["y", "yes"]:
                return True
            elif choice in ["n", "no"]:
                return False
            print("Please enter 'y' or 'n'.")

    def get_bidderDetails(self, bidderName, bidderAmount):
        self.bidderdetails[bidderName] = bidderAmount

    def get_highestBidderDetails(self, highest_bid=0):
        bidName = ""
        for biddersName, bid in self.bidderdetails.items():
            if bid > highest_bid:
                highest_bid = bid
                bidName = biddersName
        return f"\n Congratulations! {bidName.title()} wins with a bid of ${highest_bid}".title()


def main():
    print(logo)
    bid = BlindAuction()
    while True:
        bidderNameInput = bid.get_name("Enter your name: ".title())
        bidderAmountInput = bid.get_int("Enter Amount: ".title())
        bid.get_bidderDetails(bidderNameInput, bidderAmountInput)
        anyOtherBidder_input = bid.get_yes_no("Is there any other bidder ".title())
        if not anyOtherBidder_input:
            break

    print("\n==== Auction Result ====")
    print(bid.get_highestBidderDetails())
    print('Thank You for playing.'.title())

if __name__ == '__main__':
    main()
