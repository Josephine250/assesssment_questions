def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

word1 = "listen"
word2 = "silent"

print(is_anagram(word1, word2))