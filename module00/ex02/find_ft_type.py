ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

def all_thing_is_obj(object: any) -> int:
    
    if (type(object) == list):
        print("List : <class 'list'>")
    elif (type(object) == tuple):
        print("Tuple : <class 'tuple'>")
    elif (type(object) == set):
        print("Set : <class 'set'>")
    elif (type(object) == dict):
        print("Dict : <class 'dict'>")
    elif (type(object) == str):
        print(f"{object} is in the kitchen : <class 'str'>")
    else :
        print("Type not found")
    return 42

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))