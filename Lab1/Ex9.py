def commonLetter(common):
    letter = {}

    newWord1 = common.lower()
    newWord = newWord1.replace(" ", "")

    for i in newWord:
        if i in letter:
            letter[i] += 1
        else:
            letter[i] = 1
    result = max(letter, key=letter.get)

    return result


word = "111 3442 1111 32 11"

print("The most common letter is: " + str(commonLetter(word)))

print("")
