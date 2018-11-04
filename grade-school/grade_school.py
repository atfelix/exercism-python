from functools import reduce

class School(object):
    def __init__(self, name, num_grades=9):
        self.grades = [[] for _ in range(num_grades)]

    def grade(self, level):
        return tuple(self.grades[level - 1])

    def add(self, person, level):
        self.grades[level - 1].append(person)

    def sort(self):
        all_students = []
        for level, grade in filter(lambda x: x[1], zip(range(1, 10), self.grades)):
            all_students.append((level, tuple(sorted(grade))))
        
        return all_students