#10.8
def book(file):
	"""A function with single variable file"""
	text = ""
	with open(file, encoding='utf-8') as file:
		for lines in file:
			text += lines.lower()
	words_all = text.split()
	words = set(words_all)
	print(len(words))
	print(len(words_all))
	dictionary = {
				
		}
	for word in words:
		count = int(text.count(word))
		dictionary[count] = word
	#print(dictionary)
	counts = []
	for key in dictionary.keys():
		counts.append(key)
	counts_final = sorted(counts, reverse = True)
	for n in range(0, 51):
		count_n = counts_final[n]
		word_n = dictionary[count_n]
		print(f"{word_n} = {count_n}")
book('harry.txt')