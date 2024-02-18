def to_rna(dna_strand):
	rna = ""
	for base in dna_strand:
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