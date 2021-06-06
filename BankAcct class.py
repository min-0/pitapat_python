class BankAcct:
    def __init__(self, money=0):
        self.money = money

    def deposit(self, add):
        self.add = add
        self.money += self.add

    def withdraw(self, sub):
        self.sub = sub
        if self.sub > self.money:
            print('인출 불가: 잔고가 부족함')
        else:
            self.money -= self.sub

    def balance(self):
        return self.money


a = BankAcct(1000)
print(a.balance())

a.deposit(100)
print(a.balance())

a.withdraw(500)
print(a.balance())

a.withdraw(1000)
