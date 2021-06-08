# 01
def dbl(x):
    return x * 2


print(dbl(7))

# 02


def mul(arg1, arg2): return arg1 * arg2


print('곱셈 값:', mul(10, 20))
print('곱셈 값:', mul(37, 29))

# 03


def nestfunc(n):
    return lambda x: x * n


dbl = nestfunc(2)
tri = nestfunc(3)

print(dbl(25))
print(tri(10))
