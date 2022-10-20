def gen(lista, x=1, flag=True):
    solution = []
    for currStr in lista:
        currSol = []
        for ascii in currStr:
            if (ord(ascii) % x == 0 and flag) or (ord(ascii) % x != 0 and flag == False):
                currSol.append(ascii)
        if currSol:
            solution.append(currSol)

    return solution


print(gen(["test", "hello", "lab002"], 2, False), end="\n\n")