# 실전문제 3.37

def points(x1, y1, x2, y2):
    if (x2-x1) == 0:
        slope = "infinity"
    else:
        slope = (y2-y1)/(x2-x1)

    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

    print("The slope is", slope, "and the distance is", distance)


x1, y1, x2, y2 = map(int, input().split())
# 값을 한 줄에 한 번에 입력 받기 위해 map 함수와 split 함수를 사용

points(x1, y1, x2, y2)
