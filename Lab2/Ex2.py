def prime_numbers(number):
    if number > 1:
        for i in range(2, number//2):
            if number % i == 0:
                break
        else:
            print(number, end=" ")


def list_of_numbers(list_of_elem):
    new_list = []

    for i in list_of_elem:
        prime_numbers(i)

    print(end="\n")
    return new_list


list_of_elem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The prime numbers are: ", end="")
list_of_numbers(list_of_elem)