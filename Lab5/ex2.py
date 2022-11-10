def sum(*args, **kwargs):

    s = 0

    for kw in kwargs.keys():
        s += int(kwargs[kw])

    return s


anom_function = lambda *args, **kwargs: sum([val for val in kwargs.values()])

print(sum(1,2,c=3,d=4))
