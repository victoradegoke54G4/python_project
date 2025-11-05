
def sentence_maker(textInput):
    '''returns a sentence with marks'''
    capitalized_text = textInput
    question_words = ['How', 'What', 'Why', 'Where', 'Who']
    for words in question_words:
        if textInput.startswith(words):
            return '{}?\n'.format(capitalized_text)
    return '{}.\n'.format(capitalized_text)


def main():
    '''allows users to interact with the app'''
    print('WELCOME TO THE STORY GENERATOR APP.')
    sentence_box = ''
    while True:
        userInput = input('What is on Your Mind? Input \'\\end\' to terminate program: ').capitalize()
        if not userInput:
            print('Check Your Input')
        elif userInput == '\\end':
            print()
            break
        else:
            sentence = sentence_maker(userInput)
            sentence_box += sentence
    print(sentence_box, '\n')
    print('Thank You for using the app.')
main()