import sys

argv = sys.argv


def main():
    errorStr = "AssertionError: the arguments are bad"
    try:
        if (len(argv) < 3 or len(argv) > 3):
            raise AssertionError
        else:
            print("good")
    except AssertionError:
        print(errorStr)


if __name__ == "__main__":
    main()
