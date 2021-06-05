# 7.1
# def f(y):
#   x = 2
#    print('In f(): x = {}, y = {}'.format(x, y))
#    g(3)
#    print('In f(): x = {}, y = {}'.format(x, y))
# def g(y):
#    x = 4
#    print('In g(): x = {}, y = {}'.format(x, y))
# f(1)

# 7.2
# def f(y):
#    x = 2
#    return g(x)
# def g(y):
#    global x
#    x = 4
#    return x*y
#x = 0
#res = f(x)
#print('x = {}, f(0) = {}'.format(x, res))

# 7.3
# def safe_opne(filename, mode):
#    try:
#        infile = open(filename, mode)
#        return infile
#    except:
#        return None

# 7.4

# def h(n):
#     print('Start h')
#     try:
#         print(1/n)  # 오류가 발생하는 문장
#     except:
#         print('Caught!')
#     print(n)

# def g(n):
#     try:
#         print('Start g')
#         try:
#             h(n-1)
#         except:
#             print('Caught!')
#         print(n)
#     except:
#         print('Caught!')

# def f(n):
#     print('Start f')
#     g(n-1)
#     print(n)

# f(2)
