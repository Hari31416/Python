import inflect
p = inflect.engine()
print(len(p.number_to_words(115)))
words = []
words_count = []
for n in range(1,1001):
    word = p.number_to_words(n)
    word1= word.replace(' ', '')
    word2 = word1.replace('-', '')
    word3 = word.replace(',', '')
    words.append(word3)

for w in words:
    words_count.append(len(w))
print(sum(words_count))