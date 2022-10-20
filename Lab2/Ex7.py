def tuples(list_of_numbers):
    tuples_of_2_elem = ()
    list_of_pal = []
    count = 0

    for i in list_of_numbers:
        copy_number = i
        new_number = 0

        while i > 0:
            helper = i % 10
            new_number = new_number * 10 + helper
            i = i // 10

        if copy_number == new_number:
            count += 1
            list_of_pal.append(copy_number)

    tuples_append = tuples_of_2_elem + (count,)

    var = max(list_of_pal)
    tuples_append = tuples_append + (var,)

    print("My tuple with numbers of palindroms and the greatest one is: " + str(tuples_append), end="\n\n")


list_of_palindroms = [121, 3321, 3113, 1421421, 1221, 414]
tuples(list_of_palindroms)