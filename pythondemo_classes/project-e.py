class bank:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.__acc_no = account_no

    def check_bal(self):
        print(self.balance)

    def deposite(self, amount):
        self.balance = self.balance + amount

    def show_me_acc_no(self):
        print(self.__acc_no)


bnk = bank(6000, 48635825624752)
bnk.deposite(5000)
bnk.check_bal()
print(bnk.balance)
