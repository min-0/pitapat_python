# 실습문제 3.11

def allEven(iArray):
    cnt = 0
    for i in iArray:
        if int(i) % 2 == 0:
            cnt += 1
    if(cnt == len(iArray)):
        return True
    else:
        return False


iArray = input().split()
# print(type(iArray)) list type
# iArray1 = input()
# print(type(iArray1)) str type

print(allEven(iArray))
