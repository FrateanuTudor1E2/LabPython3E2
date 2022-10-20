def occurences(string1, string2):
    word = 0
    first_word = string1.split()
    second_word = string2.split()

    for i in range(len(first_word)):
        for j in range(len(second_word)):
            if first_word[i].lower() == second_word[j].lower():
                word += 1

    return word


string1 = 'aba'
string2 = 'b aba bbc aba aba'

print("")
print("De cate ori gasim stringul 1 in stringul 2: " + str(occurences(string1, string2)))
print("")
