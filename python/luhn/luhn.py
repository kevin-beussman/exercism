class Luhn(object):

	def __init__(self, numstr):
		self.numstr = numstr.replace(" ","") # remove spaces

	def addends(self):
		luhn_num = []
		double = 1
		for i in range(len(self.num) - 1, -1, -1):
			digit = self.num[i] * double
			if digit > 9:
				digit -= 9
			luhn_num.insert(0, digit)

			if double == 1:
				double = 2
			elif double == 2:
				double = 1
		return luhn_num

	def checksum(self):
		return (sum(self.addends())) % 10

	def valid(self):
		if (self.numstr.isnumeric()) and (self.numstr != "0"):
			self.num = [int(digit) for digit in self.numstr]
			return self.checksum() == 0
		else:
			return False