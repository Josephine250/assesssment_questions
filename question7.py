def find_longone(sentence):
    words = sentence.split()
    long = words[0]

    for word in words:
        if len(word) > len(long):
            long = word

    return long


sentence = "i love your languages"

print(find_longone(sentence))