# def sub(x, y):
#     global a

#     a = 5
#     x, y = y, x
#     b = 6
#     print(a, b, x, y)


# a, b, x, y = 1, 2, 3, 4
# sub(x, y)
# print(a, b, x, y)

# for k in range(1, 17):
#     if k % 3 == 0:
#         print(k, end=' ')

# i = 2
# j = 1
# k = 3

# if i > j:
#     if i > k:
#         print('A')
# else:
#     print('B')
# print('C')
# import turtle


# def Test(n):
#     t = turtle.Turtle()
#     t.shape('square')
#     for i in range(n):
#         for k in range(3):
#             t.forward(50)
#             t.right(120)
#         t.right(60)


# Test(6)

# m = [3, 6, 4, 2, 7, 8, 1]
# print(m[2:5])

# t = eval(input('>>'))
# sec = t % 60
# mi = (t//60) % 60
# hou = (t//60)//60

# print(hou, "시", mi, "분",  sec, "초")

for k in range(1, 7):
    for i in range(1, k):
        if k % 2 == 0:
            break
        print(i, end=' ')
    else:
        print(k)
