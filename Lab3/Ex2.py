def string_dictionary(s):
    return {i: s.count(i) for i in set(s)}


s = "Ana has apples"

print(string_dictionary(s))
