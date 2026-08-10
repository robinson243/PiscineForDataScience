import sys

argv = sys.argv  
  
def countLower(str) -> int:
    lowerCase = 0
    for char in str:
        if char.islower():
            lowerCase+=1
    return lowerCase

def countUpper(str) -> int:
    upperCase = 0
    for char in str:
        if char.isupper():
            upperCase+=1
    return upperCase

def punctuationCount(str) -> int:
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    punctuationMarks = 0
    for c in str:
        if c in punctuation:
            punctuationMarks += 1
    return punctuationMarks


def digitCount(str) -> int:
    digits = 0
    for c in str:
        if c.isdigit() == True:
            digits += 1
    return digits


def building():
    countSpace = 0
    if (len(argv) > 2):
        print(AssertionError("AssertionError: more than one argument is provided"))
    elif (len(argv) <= 2):
        if len(argv) == 1 or not argv[1]:
            str = input("Write a sentence > ")
        else:
            str = argv[1]
        countSpace = str.count(" ")
        print(f"The text contains {len(str)} characters:")
        print(f"{countUpper(str)} lower letters")
        print(f"{countLower(str)} upper letters")
        print(f"{punctuationCount(str)} punctuation marks")
        print(f"{countSpace} spaces")
        print(f"{digitCount(str)} digits")


building()