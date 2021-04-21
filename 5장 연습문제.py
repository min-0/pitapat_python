# 5.12
# def test(n):
#     if n == 0:
#         print('Zero')
#     elif n < -1:
#         print('Negative')
#     else:
#         print('Positive')
# n = eval(input('수 입력>>'))
# test(n)

# 5.14
# def mult3(n):
#     for i in n:
#         if i % 3 == 0:
#             print(i)
#     print()
# n = list(map(int, input().split()))
# mult3(n)

# 5.15
# def vowels(s):
#     for i in range(len(s)):
#         if s[i] in 'aeiouAEIOU':
#             print(i)
# s = input()
# vowels(s)

# 5.16
# def indexes(alpha, s):
#     lst = []
#     for i in range(len(s)):
#         if s[i] in alpha:
#             lst.append(i)
#     return lst
# alpha = input()
# s = input()
# print(indexes(alpha, s))

# 5.17
# def doubles(lst):
#     for k in range(1, len(lst)):
#         if (lst[k-1])*2 == lst[k]:
#             print(lst[k])
# lst = list(map(int, input().split()))
# doubles(lst)

# 5.18
# def four_letter(word):
#     lst = []
#     for i in word:
#         if len(i) == 4:
#             lst.append(i)
#     return lst
# word = input().split()
# print(four_letter(word))

# 5.19
# def inBoth(lst1, lst2):
#     for i in range(len(lst1)):
#         if lst1[i] in lst2:
#             return True
#     return False
# lst1 = list(map(int, input('lst1>>').split()))
# lst2 = list(map(int, input('lst2>>').split()))
# print(inBoth(lst1, lst2))

# 5.20
# def intersect(lst1, lst2):
#     res = []
#     for i in range(len(lst1)):
#         if lst1[i] in lst2:
#             res.append(lst1[i])
#     return res
# lst1 = list(map(int, input('lst1>>').split()))
# lst2 = list(map(int, input('lst2>>').split()))
# print(intersect(lst1, lst2))

# 5.21
# def pair(lst1, lst2, n):
#     for i in range(len(lst1)):
#         for k in range(len(lst2)):
#             if n == lst1[i]+lst2[k]:
#                 print(lst1[i], lst2[k])
# lst1 = list(map(int, input('lst1>>').split()))
# lst2 = list(map(int, input('lst2>>').split()))
# n = int(input('n>>'))
# pair(lst1, lst2, n)

# 5.22
# def pairSum(lst, n):
#     for i in range(len(lst)-1):
#         for k in range(i, len(lst)):
#             if n == lst[i]+lst[k]:
#                 print(i, k)
# lst = list(map(int, input('lst>>').split()))
# n = int(input('n>>'))
# pairSum(lst, n)
