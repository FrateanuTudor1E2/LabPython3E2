def wordCounter(sentence):
    word_counter = 0
    j = len(sentence)

    newSentence = sentence.split()

    for i in newSentence:
        word_counter += 1

    return word_counter


sentence = "I have Python exam "

print("The number of words is: " + str(wordCounter(sentence)))

print("")