def printName(x):
    for name, value in globals().items():
        if not name.startswith("__") and value is x:
            print(name, end='')

def NULL_not_found(object: any) -> int:
    if object == None:
        printName(object)
        print(f" : {object} <class 'NoneType'>")
    elif type(object) == float and object != object:
        printName(object)
        print(f" : {object} <class 'float'>")
    elif type(object) == bool:
        printName(object)
        print(f" : {object} <class 'bool'>")
    elif type(object) == int:
        printName(object)
        print(f" : {object} <class 'int'>")
    elif object == "":
        printName(object)
        print(f" : {object} <class 'str'>")

    else:
        print("Type not Found")
    return 1
