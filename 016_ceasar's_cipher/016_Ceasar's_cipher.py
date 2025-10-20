
from ceasar_ascii_logo import logo

class Ceasar_Cipher:
    def __init__(self, p_message, p_shift):
        self.message = p_message.upper()
        self.shift = p_shift
        alphabet = ('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z').split(',')
        self.alphabet = alphabet
        
    def encryption(self):
        cipher = ''
        for char in  self.message:
            position= self.alphabet.index(char)
            new_position = (position + self.shift) % 26
            new_char = self.alphabet[new_position]
            cipher +=new_char
        return 'The encrypted message is {}. '. format(cipher)

    def decryption(self) :
        decipher =''
        for char in self.message:
            position = self.alphabet.index(char)
            normal_position = (position - self.shift) % 26
            normal_char = self.alphabet[normal_position]
            decipher += normal_char
        return 'The decrypted message is {}.'.format(decipher)

def getint(prompt):
    while True:
        try:
            return int(float(input(prompt)))
        except ValueError:
            print('Invalid Value.')
        except TypeError:
            print('Check Type Input.')

# create user interface
def main():
    '''allows user to interact with the app'''
    print(logo)
    #create object
    while True:
        encrypt_decryptInput = input('\nType \'E\' to encrypt and \'D\' to decrypt message: ').upper()
        if not encrypt_decryptInput or not encrypt_decryptInput.isalpha():
                print('Check Input')
        else:
            if encrypt_decryptInput == 'E':
                encrypt_messageInput = input('Enter the message you want to encrypt: ').upper().strip()
                encrypt_shift_number = getint('Enter your shift number: ')
                Ceasars_Cipher = Ceasar_Cipher(encrypt_messageInput,  encrypt_shift_number)
                print (Ceasars_Cipher.encryption())

            else:
                decrypt_messageInput = input('Enter the message you want to decrypt: ').upper().strip()
                decrypt_shift_number = getint('Enter your shift number: ')
                Ceasars_Cipher = Ceasar_Cipher(decrypt_messageInput, decrypt_shift_number)
                print(Ceasars_Cipher.decryption())
                
        exit_messageInput = input('Do you wish to continue? y/n: ').upper()
        if not exit_messageInput or not exit_messageInput.isalpha():
            print('Check Input')
        else:
            if exit_messageInput == 'N':
                break
    print('Thank You For Using The App.')

if __name__ == '__main__':
        main()