scores = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1)
scores.update(dict.fromkeys(['D', 'G'], 2))
scores.update(dict.fromkeys(['B', 'C', 'M', 'P'], 3))
scores.update(dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4))
scores.update({'K':5})
scores.update(dict.fromkeys(['J', 'X'], 8))
scores.update(dict.fromkeys(['Q', 'Z'], 10))

def score(word):
    if not word.isalpha():
        return 0
    return sum([scores[letter] for letter in word.upper()])