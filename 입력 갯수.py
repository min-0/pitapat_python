c = input('문자열 입력: ')
st = set(c)

for k in st:
    i = 0
    for n in c:
        if k == n:
            i += 1
    print(k, ': ', i, '회')
