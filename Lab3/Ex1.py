def AB(a, b):
    return set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b) - set(a)


A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]
print(AB(A, B))
