class circle:
    def area(self):
        r = float(input("enter radius of circle"))
        cal = 3.14 * r * r
        print("area of circle is", cal)


c = circle()
c.area()
