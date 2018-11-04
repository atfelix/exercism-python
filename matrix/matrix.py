class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = self.parse(matrix_string)
    
    def parse(self, matrix_string):
        return [list(map(int, row.split())) for row in matrix_string.split('\n')]

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return list(self.rows[j][index] for j in range(len(self.rows)))
