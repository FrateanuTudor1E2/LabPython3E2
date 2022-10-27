def unianddupli(lista):
    return len(set(lista)), len(lista) - len(set(lista))


A = [1, 2, 2, 3, 4, 4]
B = [5, 5, 5, 5, 5]
print(unianddupli(A))
print(unianddupli(B))
