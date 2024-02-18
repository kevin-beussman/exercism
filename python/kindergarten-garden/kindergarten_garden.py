plant_definitions = {"G":"Grass", "C":"Clover", "R":"Radishes", "V":"Violets"}

class Garden:

    def __init__(self, plant_list, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.plant_list = plant_list
        students.sort()
        self.students = students
    
    def plants(self, student):
        plant_split = self.plant_list.split('\n')

        plant_sect = [plant_split[0][(self.students.index(student) * 2):(self.students.index(student) * 2 + 2)], plant_split[1][(self.students.index(student) * 2):(self.students.index(student) * 2 + 2)]]
        
        return [plant_definitions[letter] for letter in list("".join(plant_sect))]