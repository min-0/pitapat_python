class BankAccount:
    money = 0.0

    def __init__(self, money):
        self.money = money

    def withdraw(self, money):
        self.money = self.money - money

    def deposit(self, money):
        self.money = self.money + money

    def balance(self):
        return self.money


money = eval(input("초기 금액 입력: "))
bank = BankAccount(money)
print("{:.2f}".format(bank.balance()))
money = eval(input("인출 금액 입력: "))
bank.withdraw(money)
print("{:.2f}".format(bank.balance()))
money = eval(input("예금 금액 입력: "))
bank.deposit(money)
print("{:.2f}".format(bank.balance()))
