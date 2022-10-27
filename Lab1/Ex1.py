def cmmdc(x, y):
    if (y == 0):
        return abs(x)
    else:
        return cmmdc(y, x % y)


l = [int(l) for l in input().split()]
a = int(l[0])
b = int(l[1])
cm1 = cmmdc(a, b)
for i in range(2, len(l)):
    cm1 = cmmdc(cm1, l[i])
print(cm1)
