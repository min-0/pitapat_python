for i in range(1, 6):
    for k in range(i-6, -1):
        print(' ', end='')
    for j in range(1, i*2):
        print('*', end='')
    print()
