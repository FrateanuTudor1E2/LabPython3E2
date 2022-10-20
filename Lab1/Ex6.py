def palindrom(number):
    copy_number = number
    new_number = 0

    while number > 0:
        helper = number % 10
        new_number = new_number * 10 + helper
        number = number // 10

    if copy_number == new_number:
        print(str(copy_number) + " este palindrom ")
    else:
        print(str(copy_number) + " nu este palindrom ")


palindrom(1221)
print("")