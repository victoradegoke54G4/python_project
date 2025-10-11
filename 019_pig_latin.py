


class PigLatin:
    def __init__(self,message):
        message = []
        self.message = message
        self.prefix = ''
        self.suffix =''
        self.pigLatin = []
        self.word = ''
        self.vowels = ('a','e','i','o','u')
    @staticmethod
    def get_message(prompt):
        while True:
            message = input(prompt)
            if message:
                return message
            print('Input a Valid choice.'.capitalize())
    
    def PigLatin_prefix_nonletter(self):
        for word in self.message:
            while len(word)>0 and not word[0].isalpha():
                self.prefix += word[0]
                word = word[1:]
                self.word = word
            if len(word) == 0:
                self.pigLatin.append(word) 
    

    def PigLatin_suffix_nonletter(self):
        while len(self.word) > 0 and not self.word[-1].isalpha():
                # word = self.word
                self.suffix += self.word[-1]
                self.word = self.word[:-1]

    def pigLatinConverter(self):
        was_upper =self.word.upper()
        was_title =self.word.title()
        prefix_consonant = ''
        while self.word[0] not in self.vowels:
                prefix_consonant +=self[0]
        if prefix_consonant:
            self.word += prefix_consonant + 'ay'
        else:
             self.word += 'yay'
        if was_upper:
            self.word =self.word.upper()
        if was_title:
            self.word =self.word.title()
        
        self.pigLatin.append(self.prefix + self.word)
        self.pigLatin.append(self.suffix)



def main():
    pigLatin =PigLatin()
    print('Welcome to the pig latin converter'.upper())
    userMessage_input = pigLatin.get_message('\nEnter Your Message: ').lower().strip().split()
    PigLatin.pigLatinConverter(userMessage_input)

main()