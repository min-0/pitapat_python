def d2x(num, Funx):
    res = ''
    while num > 0:
        mod = num % Funx
        div = num // Funx
        num = div
        res += str(mod)
    return res[::-1]

# int(input("숫자를 입력하세요: "))
# int(input("변환할 진수를 입력하세요: "))


print(d2x(10, 2))
