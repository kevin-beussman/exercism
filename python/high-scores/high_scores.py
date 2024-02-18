def latest(scores):
	return scores[-1]

def personal_best(scores):
	return max(scores)

def personal_top_three(scores):
	scores_sorted = sorted(scores, reverse=True)
	# scores.sort(reverse=True) # don't do this! changes the order of scores permanently
	return scores_sorted[0:3]
