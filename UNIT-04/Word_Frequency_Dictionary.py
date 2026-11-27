sentence = input("Enter a sentence: ")
word_counts = {}

for word in sentence.lower().split():
    word_counts[word] = word_counts.get(word, 0) + 1

print("Word frequencies:")
for word, count in word_counts.items():
    print(word, ":", count)