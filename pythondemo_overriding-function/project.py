class sample:
    def add(self, n1, n2):
        n3 = n1 + n2
        print("Additio is", n3)


class sample1(sample):
    def add(self, n1, n2):
        n3 = n1 - n2
        print("sabtraction is", n3)


s = sample1()
s.add(10, 30)
