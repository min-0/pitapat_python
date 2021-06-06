class Point:
    '평면 상의 점을 표현하는 클래스'

    def __init__(self, xcord=0, ycord=0):
        '점 좌표를 (xcord, ycord)로 초기화'
        self.x = xcord
        self.y = ycord

    def setx(self):
        return self.x

    def sety(self):
        return self.y

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        '표준 문자열 표현(x, y)를 반환'
        return 'Point({},{})'.format(self.x, self.y)


a = Point(3, 4)
print(a)
print(a.setx())
print(a.sety())
print(a.get())

print(Point(3, 5) == Point(3, 5))
print(Point(3, 5) == eval(repr(Point(3, 5))))
