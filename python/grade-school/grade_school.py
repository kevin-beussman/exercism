class School:
	
	def __init__(self):
		self.db = {}
	
	def add_student(self, name, grade):
		if grade in self.db:
			self.db[grade].update(self.db[grade] | {name})
		else:
			self.db[grade] = {name}
	
	def roster(self):
		grades = list(self.db.keys())
		grades.sort()
		sorted = []
		for grade in grades:
			students = list(self.db[grade])
			students.sort()
			sorted.extend(students)
		return sorted
	
	def grade(self, grade):
		if grade in self.db:
			students = list(self.db[grade])
			students.sort()
			return students
		else:
			return []