value = 24
binary = "{0:b}".format(value)
binary = int(binary)


def binaryCounter(bin):
    index = 0

    while bin > 0:
        if bin % 10 == 1:
            index += 1
        bin = bin // 10

    return index


print("We have " + str(binaryCounter(binary)) + " bites for " + str(value))