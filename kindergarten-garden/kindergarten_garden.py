class Garden(object):

    vegetable_map = {
        "R": "Radishes",
        "C": "Clover",
        "G": "Grass",
        "V": "Violets",
    }

    def __init__(self, diagram, students=("Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginger", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry")):
        self.diagram = diagram.split()
        self.students = sorted(students)
        self.student_row_length = 2


    def plants(self, name):
        if name not in self.students:
            return []
        vegetables = []
        for row in self.diagram:
            for column in self.student_plantation(name):
                vegetables.append(Garden.vegetable_map[row[column]])
        return vegetables

    def student_plantation(self, student):
        index = self.students.index(student)
        return range(index * self.student_row_length, (index + 1) * self.student_row_length)