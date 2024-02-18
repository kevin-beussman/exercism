def to_rna(strand):
	rna = ""
	for base in strand:
		if base == "G":
			rna += "C"
		elif base == "C":
			rna += "G"
		elif base == "T":
			rna += "A"
		elif base == "A":
			rna += "U"
		else:
			print("Strand contains an invalid base pair!")
			return None
	return rna