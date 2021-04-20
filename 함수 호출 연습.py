# 첫 번재 사용자 정의 함수 교재80p
# def f(x):
#     res = x**2+1
#     return res

# x = (int)(input("정수 입력>> "))

# print(3 * f(x) + 4)

# 실습문제 3.8
#import math
# def perimeter(num):
#     res = num * 2 * math.pi
#     return res

# num = eval(input("정수 입력>> "))

# print(perimeter(num))

# 함수의 입력 인수 교재81p
# def squareSum(x, y):
#     return x**2 + y**2


# x = int(input('x입력>>'))
# y = int(input('y입력>>'))

# print(squareSum(x, y))

# 실습문제 3.9
# def average(n1, n2):
#     res = (n1+n2)/2
#     return res


# n1 = eval(input('n1>>'))
# n2 = eval(input('n2>>'))

# print(average(n1, n2))


# 함수 정의는 대입문이다 교재84p
# s = input('Enter square or cube: ')

# if s == 'sqyare':
#     def f(x):
#         return x*x
# else:
#     def f(x):
#         return x*x*x

# x = eval(input())

# print(f(x))

# 실습문제 3.16
def swqpFL(lst):
    lst[0], lst[-1] = lst[-1],  lst[0]
    print(lst)


ingredients = input("리스트에 들어갈 원소 입력>>").split()
print(swqpFL(ingredients))
