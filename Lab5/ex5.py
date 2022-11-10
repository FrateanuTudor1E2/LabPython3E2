def nb_in_list(lst):

    new_lst = []
    for el in lst:
        if type(el) in [int, float, complex]:
            new_lst.append(el)
    return new_lst

print(nb_in_list([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))