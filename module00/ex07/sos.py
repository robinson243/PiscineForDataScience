import sys
import re

av = sys.argv

NESTED_MORSE = {
    " ": "/",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
    "e": ".", "f": "..-.", "g": "--.", "h": "....",
    "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.",
    "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..",
    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----."
}

# res = bool(re.match("^(?=.*[a-zA-Z])(?=.*[\\d])[a-zA-Z\\d]+$", "A530"))


def main():
    errorStr = "AssertionError: the arguments are bad"
    try:
        if len(av) != 2 or av[1].isalnum() is False:
            raise AssertionError
        else:
            str = av[1]
            for letter in str:
                print(NESTED_MORSE[letter])
                # print(letter)

    except AssertionError:
        print(errorStr)


if __name__ == "__main__":
    main()
