class PigLatin:
    def __init__(self, message):
        self.original_message = message
        self.words = message.split()
        self.vowels = ('a','e','i','o','u')
        self.translated_words = []

    @staticmethod
    def get_message(prompt):
        while True:
            message = input(prompt).strip()
            if message:
                return message
            print(" Please enter a valid message.")


    def extract_non_letters(self, word):

        prefix, suffix = '', ''

        while len(word) > 0 and not word[0].isalpha():
            prefix += word[0]
            word = word[1:]

        while len(word) > 0 and not word[-1].isalpha():
            suffix = word[-1] + suffix
            word = word[:-1]

        return prefix, word, suffix

    def detect_case(self, word):
        """Return the word's casing type."""
        return word.isupper(), word.istitle()

    def restore_case(self, word, was_upper, was_title):
        """Restore word to its original casing."""
        if was_upper:
            return word.upper()
        elif was_title:
            return word.title()
        return word

    def to_piglatin(self, word):
        if not word:
            return word

        was_upper, was_title = self.detect_case(word)
        word = word.lower()

        if word[0] in self.vowels:
            word = word + "yay"
        else:
            consonant_cluster = ''
            while len(word) > 0 and word[0] not in self.vowels:
                consonant_cluster += word[0]
                word = word[1:]
            word = word + consonant_cluster + "ay"

        return self.restore_case(word, was_upper, was_title)

    def process_word(self, word):
        prefix, clean_word, suffix = self.extract_non_letters(word)
        pig_word = self.to_piglatin(clean_word)
        return prefix + pig_word + suffix

    def convert(self):

        for word in self.words:
            translated = self.process_word(word)
            self.translated_words.append(translated)
        return ' '.join(self.translated_words)

    def show_result(self):
        """Display the Pig Latin translation."""
        translated_text = self.convert()
        print(f"\n Pig Latin Translation: {translated_text}")


def main():
    print("\nWELCOME TO THE PIG LATIN CONVERTER ")
    message = PigLatin.get_message("Enter your message: ")
    piggy = PigLatin(message)
    piggy.show_result()


if __name__ == "__main__":
    main()
