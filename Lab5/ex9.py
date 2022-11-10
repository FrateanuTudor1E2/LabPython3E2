def list_of_dict(pairs):

    return [{"sum": pair[0] + pair[1],
             "prod": pair[0]*pair[1],
             "pow": pair[0]**pair[1]} for pair in pairs]

print(list_of_dict(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]))