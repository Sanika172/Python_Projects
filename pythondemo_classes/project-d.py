class stud_info:
    def getdata(self):
        self.name = input("enter your name")
        self.rno = int(input("enter your roll number"))
        self.mob = int(input("enter your mobile no"))
        self.add = input("enter your address")

    def dislpay(self):
        print("your name is", self.name)
        print("your roll no is", self.rno)
        print("your mobile no is", self.mob)
        print("your address is", self.add)


std = stud_info()
std.getdata()
std.dislpay()
