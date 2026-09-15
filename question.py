def find_longest(sentences):
        words = sentences.split()
        longest = words[0]
        for word in words:
                if len(word) > len(longest):
                  longest = word
        return longest
sentences =" i like programming challenges "
print(find_longest(sentences))