import sys

tab = sys.argv

if (len(tab) > 2):
    print(AssertionError("AssertionError: more than one argument is provided"))
elif (len(tab) == 2):
    try :
        num = int(sys.argv[1])
        if(num % 2 == 1):
            print("I'm Odd.")
        else :
            print("I'm Even.")
    except ValueError :
        print("AssertionError: argument is not an integer")