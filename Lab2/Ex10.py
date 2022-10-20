import numpy as np
def make_a_tuple(lists):
    tuple_output = ()

    input_lists = list(lists)

    max_tuple = max([len(x) for x in input_lists])

    for input_list in input_lists:
        if len(input_list) < max_tuple:
            input_list.extend(None for _ in range(len(input_list), max_tuple))

    transpusa = np.reshape(list_of_elements, (len(lists), len(lists[0])))
    transpusa = transpusa.transpose()

    rows = len(transpusa)
    columns = len(transpusa[0])

    for i in range(rows):
        for j in range(columns):
            tuple_output = tuple_output + (transpusa[i][j],)
        print(tuple_output, end="\n")
        tuple_output = ()
    print(end="\n")
    # .


list_of_elements = [1, 2, 3, 4], [5, 6, 7], ["a", "b", "c"]
make_a_tuple(list_of_elements)