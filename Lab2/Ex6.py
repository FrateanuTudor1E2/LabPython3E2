def exactlyX(list_of_lists, x):
    new_list = []
    last = -1
    count = 0
    final_list = []
    for i in list_of_lists:
        new_list.extend(i)

    for i in new_list:
        var = new_list.count(i)
        if var == x and i not in final_list:
            print(str(i) + " appears exactly " + str(var) + " times", end="\n\n")
            final_list.append(i)


list_of_lists = [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]
x = 2
exactlyX(list_of_lists, x)