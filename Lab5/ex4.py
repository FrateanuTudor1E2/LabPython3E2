def dictionaries(*args, **kwargs):
    return_list = []

    for arg in args:
        if type(arg) == dict:
            if len(arg.keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 else False
                                             for key in arg.keys()]):
                return_list.append(arg)

    for kw in kwargs.keys():
        if type(kwargs[kw]) == dict:
            if len(kwargs[kw].keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 else False
                                                    for key in kwargs[kw].keys()]):
                return_list.append(kwargs[kw])

    return return_list

print(dictionaries( {1: 2, 3: 4, 5: 6},

 {'a': 5, 'b': 7, 'c': 'e'},

 {2: 3},

 [1, 2, 3],

 {'abc': 4, 'def': 5},

 3764,

 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

 test={1: 1, 'test': True}))