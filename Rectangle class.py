class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return self.height * 2 + self.width * 2


rect = Rectangle()
print(rect.getArea())
print(rect.getPerimeter())
rect2 = Rectangle(3, 4)
print(rect2.getArea())
print(rect2.getPerimeter())
