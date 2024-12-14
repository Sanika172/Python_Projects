class student:
    def __init__(self):
        self.name = input("enter your name")
        self.rno = int(input("enter your roll number"))
        self.add = input("enter your address")

    def display_info(self):
        print("your name is", self.name)
        print("your roll number is", self.rno)
        print("your address is ", self.add)


std = student()
std.display_info()
