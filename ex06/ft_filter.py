import sys

argv = sys.argv


def main():
    errorStr = "AssertionError: the arguments are bad"
    myList = []
    try:
        if (len(argv) < 3 or len(argv) > 3):
            raise AssertionError
        else:
            try:
                n = int(argv[2])
                print("good")
            except ValueError:
                print("AssertionError: the arguments are bad")
    except AssertionError:
        print(errorStr)


if __name__ == "__main__":
    main()
