
sen = input("Enter a sentence: ")
key_word = input("Enter the word to show it's occurrences: ")
words = sen.split()

word_cnt = 0
for word in words:
    if key_word in word:
        word_cnt += 1

print("number of words contain:", word_cnt)

word_cnt = 0
for word in words:
    if key_word == word:
        word_cnt += 1
print("number of exact word occurrences :", word_cnt)


