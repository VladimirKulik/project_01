class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[None for _ in range(columns)] for _ in range(rows)]

    def set_value(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.matrix[row][column] = value

    def replace_value(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            if self.matrix[row][column] is not None:
                self.matrix[row][column] = value

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def display(self):
        for row in self.matrix:
            print(row)
matrix = Matrix(10, 10)

matrix.set_value(0, 0, 1)
matrix.set_value(5, 5, 2)
matrix.set_value(9, 9, 3)

matrix.replace_value(5, 5, 4)

print("Number of rows:", matrix.get_rows())
print("Number of columns:", matrix.get_columns())

matrix.display()