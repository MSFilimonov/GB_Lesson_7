class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        for row in self.data:
            for i in row:
                print(f"{i}", end=" ")
            print()
        return ''

    def __add__(self, other):
        for row in range(len(self.data)):
            for i in range(len(self.data[row])):
                self.data[row][i] = self.data[row][i] + other.data[row][i]
        return Matrix.__str__(self)


mtr1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mtr2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mtr1.__add__(mtr2))
