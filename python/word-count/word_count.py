def count_words(sentence):
	
	word = ""
	word_dict = {}
	for i in range(0, len(sentence)):
		
		# make sentence lowercase
		char = sentence.lower()[i]
		
		# skip any formatting characters e.g. \n \t
		if char == "\\":
			i += 1
			word = ""
			continue
		
		# add alphas or digits or apostrophes to word
		elif char.isalpha() or char.isdigit() or char=="'":
			word += char
			if i < len(sentence)-1:
				continue # keep adding characters until we hit something weird
			
		# if you make it this far, you should be a word!
		if word != "":
			
			# if first or last characters are apostrophes, remove them
			while word[0]=="'":
				word = word[1:]
			while word[-1]=="'":
				word = word[:-1]
			
			if word in word_dict:
				word_dict[word] += 1
			else:
				word_dict[word] = 1
			word = ""
	
	return word_dict