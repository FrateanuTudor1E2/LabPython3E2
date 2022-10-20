def intersection(a, b):
    list_of_intersection = []
    for i in a:
        for j in b:
            if i == j:
                list_of_intersection.append(i)
    return list_of_intersection


def reunion(a, b):
    list_of_reunion = a + b
    final_list = []
    for i in list_of_reunion:
        if i not in final_list:
            final_list.append(i)

        final_list.sort()
    return final_list


def a_minus_b(a, b):
    a_minus_b_list = []
    for i in a:
        if i not in b:
            a_minus_b_list.append(i)
    return a_minus_b_list


def b_minus_a(a, b):
    b_minus_a_list = []
    for i in b:
        if i not in a:
            b_minus_a_list.append(i)
    return b_minus_a_list


a = [2, 3, 4, 5, 6, 7, 12, 14]
b = [1, 3, 5, 7, 9, 12]
print("The intersection of a and b is: " + str(intersection(a, b)), end="\n")
print("The union of a and b is: " + str(reunion(a, b)), end="\n")
print("A minus B is: " + str(a_minus_b(a, b)), end="\n")
print("B minus A is: " + str(b_minus_a(a, b)), end="\n\n")