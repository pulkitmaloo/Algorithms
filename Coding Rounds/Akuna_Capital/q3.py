def q2(input_lines):
	from collections import Counter
	import string
	words = input_lines.split()
	words_dict = Counter(words)
	letters_dict = Counter(input_lines)
	for x in string.ascii_lowercase:		
		if x not in letters_dict:
			letters_dict[x] = letters_dict.get(x, 0)

	res = str(sum(words_dict.values())) + "\nwords"
	word_keys = sorted(words_dict.keys())
	for key in word_keys:
		res += "\n" + key + " " + str(words_dict[key])
	
	res += "\nletters"
	letters_keys = sorted(letters_dict.keys())
	for key in letters_keys:
		if key not in string.ascii_lowercase:
			continue
		res += "\n" + key + " " + str(letters_dict[key])
	return res

if __name__ == "__main__":
	str_input = "a to the four where supers i be the other four"
	print(q2(str_input))