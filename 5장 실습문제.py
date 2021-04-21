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
#     if len(lst) < 2:
#         return Frue
#     else:
#         minur = lst[1] - lst[0]
#         for i in range(1, len(lst)-1):
#             if (lst[i+1] - lst[i] != minur):
#                 return False
#             else:
#                 return True
# lst = list(map(int, input().split()))
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
# def xmult(lst1, lst2):
#     res = []
#     for i in lst1:
#         for k in lst2:
#             res.append(i*k)
#     print(res)
# lst1 = list(map(int, input('lst1>>').split()))
# lst2 = list(map(int, input('lst2>>').split()))
# print(lst2)
# xmult(lst1, lst2)

# 5.8
# def bubblesort(lst):
#     for i in range(len(lst)-1, 0, -1):
#         for k in range(i):
#             if lst[k] > lst[k+1]:
#                 lst[k], lst[k+1] = lst[k+1], lst[k]
#     return lst
# lst = list(map(int, input().split()))
# print(bubblesort(lst))

# 모듈
# def incr2D(t):
#     nrows = len(t)
#     ncols = len(t[0])
#     for i in range(nrows):
#         for k in range(ncols):
#             t[i][k] += 1
#             print(t[i][k], end=' ')
#         print()
# t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 7]]
# incr2D(t)

# 5.9
# def add2D(t, s):
#     row = len(t)
#     col = len(t[0])
#     for i in range(row):
#         for k in range(col):
#             t[i][k] += s[i][k]
#     for row in t:
#         print(row)

# num = eval(input('배열크기>>'))
# t = []
# s = []
# for i in range(num):
#     t.append(list(map(int, input('lst1>>').split())))
#     s.append(list(map(int, input('lst2>>').split())))
# add2D(t, s)
