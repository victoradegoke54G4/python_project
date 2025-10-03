class Lovecalc():

    # initializing method instances
    def __init__(self, userName, loverName):
        self.userName = userName
        self.loverName = loverName
        self.true_count = 0
        self.love_count = 0


    def lovecalc(self):
        try:
            combined_name = (self.userName + self.loverName).strip().lower()
        except TypeError:
            print('Invalid Input!')
        else:    
            for char in combined_name:
                if char in 'true':
                    self.true_count += 1
                if char in 'love':
                    self.love_count += 1
        finally:
            return str(self.true_count) + str(self.love_count)


#   user interface
def main():

    print('Welcome to the Ultimate Love Calculator.')
    userName = input('Enter Your name: ').lower()
    loverName = input('Enter Your Lover\'s name: ').lower()

    result= Lovecalc(userName, loverName)
    calc_result = result.lovecalc()
    
    print(f'Your love score is {calc_result}')
    

main()