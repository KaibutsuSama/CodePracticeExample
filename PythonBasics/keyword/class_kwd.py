class Square:

    def __init__(self, x):
        self.a = x

    def area(self):
        print(self.a * self.a)


sq = Square(12)
sq.area()
