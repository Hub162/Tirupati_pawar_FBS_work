s = input("Enter a string: ")
words = s.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
