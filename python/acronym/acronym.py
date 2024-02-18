import re

def abbreviate(phrase):
	clean_phrase = re.sub(r"'", '', phrase)
	cleaner_phrase = re.sub(r"[^A-Za-z]+", ' ', clean_phrase)
	phrase_split = cleaner_phrase.split()
	acronym = ""
	for word in phrase_split:
		if word.isupper():
			acronym += word[0]
		else:
			word = word[0].upper() + word[1:]
			acronym += re.sub(r"[^A-Z]+", '', word)
	return acronym