# 5.23
# def pay(wage, hour):
#     sum = 0
#     if(hour > 60):
#         sum += (40 * wage) + (hour - 41)*(wage*1.5) + (hour - 60) * (wage * 2)
#     elif(hour > 40 and hour <= 60):
#         sum += (40 * wage) + (hour - 40)*1.5*wage
#     else:
#         sum += hour * wage
#     return sum
# wage, hour = map(int, input().split())
# print(pay(wage, hour))

# 5.24
# def case(word):
#   if(word[0]>='A' and word[0]<='Z'):
#     print('captitalized')
#   elif(word[0]>='a' and word[0]<='z'):
#     print('not capitalized')
#   else:
#     print('unknow')
# word = input('word>>')
# case(word)

# 5.25
# def leap(year):
#   if(year%4 == 0 and year%100 != 0 or year%400 == 0):
#     return True
#   else: return False
# year = int(input('year>>'))
# print(leap(year))

# 5.26
# def rps(user1, user2):
#   if(user1 == 'R' and user2 == 'R' or user1 == 'S' and user2 == 'S' or user1 == 'P' and user2 == 'P'):
#     return 0
#   elif(user1 == 'R' and user2 == 'S' or user1 == 'S' and user2 == 'P' or user1 == 'P' and user2 == 'R'):
#     return -1
#   elif(user1 == 'S' and user2 == 'R' or user1 == 'P' and user2 == 'S' or user1 == 'R' and user2 == 'P'):
#     return 1
# user1 = input('user1>>')
# user2 = input('user2>>')
# print(rps(user1, user2))

# 5.27 인덱스값으로 해도 됨
# def letter2number(grade):
#   gradeN = 0
#   if 'A' in grade:
#     gradeN += 4.0
#   elif 'B' in grade:
#     gradeN += 3.0
#   elif 'C' in grade:
#     gradeN += 2.0
#   elif 'D' in grade:
#     gradeN += 1.0
#   elif 'F' in grade:
#     gradeN = 0
#   if '+' in grade:
#     gradeN += 0.3
#   elif '-' in grade:
#     gradeN -= 0.3
#   return gradeN
# grade = input('grade>>')
# print(letter2number(grade))

# 5.28
# def geometric(lst):
#   geo = lst[1]/lst[0]
#   if len(lst) < 2:
#     return True
#   for k in range(1, len(lst)-1):
#       if lst[k+1]/lst[k] == geo:
#         return True
#   return False
# lst = list(map(int, input().split()))
# print(geometric(lst))

# 5.29
# def lastfirst(name):
#     lastname = []
#     firstname = []
#     for i in range(len(name)):
#         if ',' in name[i]:
#             lastname.append(name[i].rstrip(','))
#         else:
#             firstname.append(name[i])
#     return firstname, lastname


# name = input('name>>').split(' ')
# print(lastfirst(name))

# 5.31
# def subsetSum(lst, n):
#     sum = 0
#     for i in range(len(lst)):
#         for k in range(1, len(lst)):
#             for j in range(2, len(lst)):
#                 sum += lst[i]+lst[k]+lst[j]
#                 print(sum)
#                 if(sum == n):
#                     return True
#                 sum = 0
#     return False
# lst = list(map(int, input('lst>>').split()))
# n = int(input('n>>'))
# print(subsetSum(lst, n))

# money = eval(input('투입한 돈: '))
# pay = eval(input('물건값: '))
# res = money - pay
# print('거스름돈: ', res)
# coin500 = res//500
# coin100 = (res - (coin500 * 500))//100
# print('500원 동전의 개수: ', coin500, '\n100원 동전의 개수: ', coin100)

# for i in range(5):
#     for k in range(1, (i+1)*2):
#         print('-', end='')
#     for k in range(9, i, -2):
#         print('*', end='')
#     print()

for i in range(1, 6):
    for k in range(i-1):
        print(' ', end='')
    for k in range(6, i, -1):
        print('*', end='')
    for k in range(5, i, - 1):
        print('*', end='')
    print()
