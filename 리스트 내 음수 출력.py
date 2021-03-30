# 실습문제 3.12

def negatives(iList):
    for i in iList:
        if int(i) < 0:
            print(i)


iList = input().split()

print(negatives(iList))
