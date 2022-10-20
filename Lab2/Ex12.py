def rhyme(words):
    final_result = []
    for index in range(0, len(words)):
        list_words = list(filter(lambda item: item[-2:] == words[index][-2:], words))
        if not (list_words in final_result):
            final_result.append(list_words)
    return final_result


print(rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))