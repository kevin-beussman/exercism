def distance(strand1, strand2):
	if len(strand1) != len(strand2):
		raise ValueError("Strands have different lengths.")
	else:
		dist = 0
		for i in range(0, len(strand1)):
			if strand1[i] != strand2[i]:
				dist += 1
		return dist