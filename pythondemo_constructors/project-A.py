class circle:
    def __init__(self):
        self.pi = 3.14

    def area(self, r):
        a = self.pi * r * r
        print("area", a)


c = circle()
c.area(2)
