import sys

argv = sys.argv


def countLower(str) -> int:
    """Compte les lettres minuscules."""
    lowerCase = 0
    for char in str:
        if char.islower():
            lowerCase += 1
    return lowerCase


def countUpper(str) -> int:
    """Compte les lettres majuscules."""
    upperCase = 0
    for char in str:
        if char.isupper():
            upperCase += 1
    return upperCase


def punctuationCount(str) -> int:
    """Compte les ponctuations."""
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    punctuationMarks = 0
    for c in str:
        if c in punctuation:
            punctuationMarks += 1
    return punctuationMarks


def digitCount(str) -> int:
    """Compte les chiffres."""
    digits = 0
    for c in str:
        if c.isdigit() is True:
            digits += 1
    return digits


def main():
    """Analyse le texte fourni et gère les erreurs éventuelles."""
    countSpace = 0
    errorStr = "AssertionError: more than one argument is provided"
    try:
        if (len(argv) > 2):
            raise AssertionError
        elif (len(argv) <= 2):
            if len(argv) == 1 or not argv[1]:
                str = input("Write a sentence > ")
            else:
                str = argv[1]
            countSpace = str.count(" ")
            print(f"The text contains {len(str)} characters:")
            print(f"{countUpper(str)} upper letters")
            print(f"{countLower(str)} lower letters")
            print(f"{punctuationCount(str)} punctuation marks")
            print(f"{countSpace} spaces")
            print(f"{digitCount(str)} digits")
    except AssertionError:
        print(errorStr)
    except KeyboardInterrupt:
        print("\nctrl+c pressed")
    except EOFError:
        print("\nctrl+d pressed")


if __name__ == "__main__":
    main()
