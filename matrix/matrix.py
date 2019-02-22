class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = self.parse(matrix_string)
        self.columns = list(map(list, zip(*self.rows)))
    
    def parse(self, matrix_string):
        return [list(map(int, row.split())) for row in matrix_string.split('\n')]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
