# 5.1
# def myBMI(weight, height):
#     BMI = (weight * 703) / (height**2)
#     if(BMI < 18.5):
#         print('Underweight')
#     elif(BMI > 25):
#         print('Overweight')
#     else:
#         print('Nomal')
# weight, height = map(int, input().split())
# myBMI(weight, height)

# 5.2
# def powers(n):
#     for i in range(1, n+1):
#         print(2**i, end=' ')
# n = int(input())
# powers(n)

# 5.3
# def arithmetic(lst):
#     for i in lst:
#         if((i + 2)-(i+1) == (i+1)-i):
#             return True
#         else:
#             return False
# lst = map(int, input().split())
# print(arithmetic(lst))

# 5.4
# def factorial(n):
#     fac = n
#     if(n == 0):
#         return 1
#     else:
#         for i in range(1, n):
#             fac = fac*(n-i)
#         return fac
# n = int(input())
# print(factorial(n))

# 5.5
# def acronym(A):
#     for i in A:
#         print(i[0].upper(), end='')
# A = input().split()
# acronym(A)

# 5.6
# def divisor(n):
#     lst = []
#     for i in range(1, n+1):
#         if(n % i == 0):
#             lst.append(i)
#     print(lst)
# n = int(input())
# divisor(n)

# 5.7
def xmult(lst1, lst2):
    res = []
    for i in lst1:
        for k in lst2:
            res.append(i*k)
    print(res)


lst1 = map(int, input().split())
lst2 = map(int, input().split())
xmult(lst1, lst2)
