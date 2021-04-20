# 3.24
# lst = input().split()
# for i in lst:
#     if(i != 'secret'):
#         print(i)

# 3.25
# lst = input().split()
# for i in lst:
#     if(i[0] > 'A' and i[0] < 'M'):
#         print(i)

# 3.26
# lst = input('Enter a list: ').split()
# print("The firtst list element is ", lst[0])
# print("The last list element is " + lst[-1])

# 3.27
# n = eval(input("Enter n: "))
# for i in range(4):
#     print(i * n, end='\n')

# 3.28
# n = eval(input('Enter n: '))
# for i in range(n):
#     print(i*i)

# 3.29
# n = eval(input('Enter n: '))
# for i in range(1, n+1):
#     if(n % i == 0):
#         print(i)

# 3.30
# fn = eval(input('Enter first number: '))
# sn = eval(input('Enter second number: '))
# tn = eval(input('Enter third number: '))
# ln = eval(input('Enter last number: '))

# sum = fn + sn + tn + ln
# average = sum/4

# if(ln == average):
#     print("Equal")
# else:
#     print("Not Equal")

# 3.31
# x = eval(input('Enter x: '))
# y = eval(input('Enter y: '))
# if(x > -8 and x < 8 and y > -1 and y < 8):
#     print("It is in!")
# else:
#     print("fail")

# 3.32
# n = eval(input("Enter n:"))
# print(n//1000, (n // 100) % 10, (n % 100)//10, n % 10)
# 백의 자리는 (n % 1000)//100 == (n // 100) % 10

# 3.33
# def reverse_string(s):
#     return s[::-1]
# s = input("reverse_string>>")
# print(reverse_string(s))

# 3.34
# def pay(wage, hour):
#     if(hour > 40):
#         return (wage*40)+(hour-40)*wage*1.5
#     else:
#         return wage*hour

# wage = eval(input("시급 입력>>"))
# hour = eval(input("시간 입력>>"))
# print(pay(wage, hour))

# 3.35
# def prob(n):
#     return 1/(2**n)
# n = eval(input("n 입력>>"))
# print(prob(n))

# 3.36
# def reverse_int(n):
#     first = (n % 10)*100
#     middle = ((n//10) % 10)*10
#     last = n // 100
#     return first + middle + last
# n = eval(input("세자리 정수 입력>>"))
# print(reverse_int(n))

# 3.38
# def abbreviation(day):
#     return day[0:3]
# day = input("day:")
# print(abbreviation(day))

# 3.39
# def collision(r1, x1, y1, r2, x2, y2):
#     pita = ((x2-x1)**2)+((y2-y1)**2)
#     radius = (r1+r2)*(r1+r2)
#     if(pita <= radius):
#         return True
#     else:
#         return False
# r1, x1, y1, r2, x2, y2 = map(float, input().split())
# print(collision(r1, x1, y1, r2, x2, y2))

# 3.40
# def partition(lst):
#     for i in lst:
#         if(i[0] > 'A' and i[0] < 'M'):
#             print(i)
# lst = input().split()
# partition(lst)

# 3.41
# def lastF(FirstName):
#     return FirstName[0]
# FirstName, LastName = input().split()
# print(LastName + ", " + lastF(FirstName) + ".")

# 3.42
# def avg(lst):
#     for i in lst:
#         res = sum(i) / len(i)
#     print(res)
# stu = int(input("학생수>>"))
# lst = []
# for i in range(stu):
#     lst.append(list(map(int, input("점수>>").split())))
#     avg(lst)

# 3.43
# def hit(x, y, r, p1, p2):
#     if(x+r >= p1 and y+r >= p2):
#         return True
#     else:
#         return False
# x, y, r, p1, p2 = map(int, input().split())
# print(hit(x, y, r, p1, p2))

# 3.44
# def distance(t):
#     return (t * 340.29)/1000
# t = eval(input())
# print(distance(t))
