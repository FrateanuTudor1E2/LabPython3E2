import re


def extract(i):
    random = i
    a = re.findall("(-?\d+)", i)

    a = a[0]
    return a


i = 'aa23bb22'
print("First number character is: " + str(extract(i)))
