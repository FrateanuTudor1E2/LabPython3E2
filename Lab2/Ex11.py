def order_tuple(string_list):
    return sorted(string_list, key=lambda x: x[1][2])


print(order_tuple([('abc', 'bcd'), ('abc', 'zza')]), end="\n\n")