class Matrix:
    
	def __init__(self, data):
		self.list_rows = [x.split() for x in data.split('\n')]
				
	def row(self, index):
		return [int(j) for j in self.list_rows[index-1]]
				
	def column(self, index):
		return [int(j) for j in [self.list_rows[i][index-1] for i in range(len(self.list_rows))]]