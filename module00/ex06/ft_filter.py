def ft_filter(func, iterable):
    ("""filter(function or None, iterable) --> filter object\n\n"""
        """Return an iterator yielding those items"""
        """ of iterable for which function(item)\n"""
        """is true. If function is None, return the items that are true.""")
    if func is None:
        return [x for x in iterable if bool(x)]
    else:
        return [x for x in iterable if func(x)]


# ages = [5, 12, 17, 18, 0, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# def main():
#     adults = ft_filter(myFunc, ages)
#     for x in adults:
#         print(x)

# if __name__ == "__main__":
#     main()
