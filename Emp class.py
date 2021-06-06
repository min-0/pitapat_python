class Emp:
    empTotal = 0

    def __init__(self, name, bonus=100):
        self.name = name
        self.bonus = self.base = bonus
        Emp.empTotal += 1

    def restart(self):
        self.bonus = self.base

    def sale(self):
        self.bonus += 10

    def __str__(self):
        return '이름: ' + self.name + ' 보너스: ' + str(self.bonus)

a = Emp('peter', 50)
b = Emp('Austin')

a.sale()
print(a.name + '의 보너스: ', a.bonus)
print(b.name + '의 보너스: ', b.bonus)
print('총 직원 수: ', Emp.empTotal)

a = Emp('peter', 50)
print(a)
