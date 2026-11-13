import sys

argv = sys.argv


def lb(n):
    lambda x: len(x) > n


def ft_filter():
    """Renvoie une liste avec des mots plus grand que le nombre inscrit"""
    errorStr = "AssertionError: the arguments are bad"
    try:
        if (len(argv) < 3 or len(argv) > 3):
            raise AssertionError
        else:
            try:
                n = int(argv[2])
                str = argv[1].split()
                print([x for x in str if lb(n)])

            except ValueError:
                print(errorStr)
    except AssertionError:
        print(errorStr)
