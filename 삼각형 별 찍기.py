for i in range(1, 6):
    for k in range(i-6, -1):
        print(' ', end='')
    for j in range(1, i*2):
        print('*', end='')
    print()

print()

for i in range(1, 6):
    for k in range(i-1):
        print(' ', end='')
    for k in range(6, i, -1):
        print('*', end='')
    for k in range(5, i, - 1):
        print('*', end='')
    print()
