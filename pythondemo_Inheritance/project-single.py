# singlele Inheritance
class father:
    wife = "kalpana"
    daughter = "sanika"


class son(father):
    def display(self):
        print("my mother name is", self.wife)
        print("my sister name is", self.daughter)


s = son()
s.display()
