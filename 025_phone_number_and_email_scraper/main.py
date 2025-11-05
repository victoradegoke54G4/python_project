from data import text
import re

def phone_number_extractor(text):
    """
    Finds and returns phone numbers from text.
    Supports formats like:
    234-915-7898, (234) 915-7898, 234 915 7898 x1234
    """
    phone_regex = re.compile(r"""
        (?:\(?\d{3}\)?)         # area code (optional parentheses)
        (?:\s|-)?               # separator (space or dash)
        \d{3}                   # first 3 digits
        (?:\s|-)?               # separator
        \d{4}                   # last 4 digits
        (?:\s?(?:ext|x)\d{2,5})?  # optional extension like ext1234 or x123
    """, re.VERBOSE)

    matches = phone_regex.findall(text)
    return matches


extracted_phone_number = phone_number_extractor(text)
print('EXTRACTED PHONE NUMBERS')
for phone_number in extracted_phone_number:
    print('     '+phone_number)
print('='*18)


def email_extractor(text):
    """
    Finds and returns email from text.
    Supports formats like:
    info@gmail.com
    """
    email_regex = re.compile(r"""
        \S+
        @
        \w+ 
        \.
        \w+  
        """, re.VERBOSE)
    mo = re.findall(email_regex, text)
    return mo

extracted_email = email_extractor(text)
print()
print('EXTRACT MAIL ADRESSES')
for mail in extracted_email:
    print('     '+mail)
print()
print('HAVE A GREAT DAY')
print('='*18)