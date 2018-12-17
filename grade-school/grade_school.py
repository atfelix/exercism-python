from functools import reduce

class School(object):
    def __init__(self, num_grades=9):
        self.grades = [[] for _ in range(num_grades)]

    def grade(self, level):
        return sorted(self.grades[level - 1])

    def add_student(self, name, grade):
        self.grades[grade - 1].append(name)

    def roster(self):
        students = []
        for grade in self.grades:
            students.extend(sorted(grade))
        return students