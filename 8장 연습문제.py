# 8.10
# import math

# class Point:
#     def __init__(self, xcord=0, ycord=0):
#         self.x = xcord
#         self.y = ycord

#     def setx(self, xcord=0):
#         self.x = xcord
#         return self.x

#     def sety(self, ycord=0):
#         self.y = ycord
#         return self.y

#     def get(self):
#         return (self.x, self.y)

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __repr__(self):
#         return 'Point({},{})'.format(self.x, self.y)

#     def distance(self, other):
#         return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


# a = Point()
# print(a.setx(0))
# print(a.sety(1))

# b = Point()
# print(b.setx(1))
# print(b.sety(0))
# print(a.distance(b))

# 8.11
# class Animal:
#     def setSpecies(self, species):
#         self.spec = species

#     def setLanguage(self, language):
#         self.lang = language

#     def speak(self):
#         print('I am a{} and I {}.'.format(self.spec, self.lang))

#     def setAge(self, age):
#         self.age = age

#     def getAge(self):
#         return self.age


# flipper = Animal()
# flipper.setSpecies('dolphin')
# flipper.setAge(3)
# print(flipper.getAge())

# 8.12
# class Point:
#     def __init__(self, xcord=0, ycord=0):
#         self.x = xcord
#         self.y = ycord

#     def setx(self, xcord=0):
#         self.x = xcord
#         return self.x

#     def sety(self, ycord=0):
#         self.y = ycord
#         return self.y

#     def get(self):
#         return (self.x, self.y)

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy

#     def up(self):
#         self.move(0, 1)

#     def down(self):
#         self.move(0, -1)

#     def left(self):
#         self.move(-1, 0)

#     def right(self):
#         self.move(1, 0)

# a = Point(3, 4)
# a.left()
# print(a.get())

# 8.13
# class Rectangle:
#     def __init__(self, width=1, height=1):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def getPerimeter(self):
#         return self.height * 2 + self.width * 2


# rectangle = Rectangle(2, 4)
# print(rectangle.getPerimeter())
# rectangle = Rectangle()
# print(rectangle.area())

# 8.14
# x, y = 1, 2
# # (a)
# print(x.__gt__(y))
# # (b)
# print(x.__ne__(y))
# # (c)
# print(x.__mod__(y))
# # (d)
# print(x.__floordiv__(y))
# # (e)
# print(x.__or__(y))

# 8.15
# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def __gt__(self, other):
#         return self.rank > other.rank and self.suit > other.suit

#     def __lt__(self, other):
#         return self.rank < other.rank and self.suit < other.suit

#     def __ge__(self, other):
#         return self.rank >= other.rank and self.suit >= other.suit

#     def __le__(self, other):
#         return self.rank <= other.rank and self.suit <= other.suit


# print(Card('3', '\u2660') < Card('8', '\u2662'))
# print(Card('3', '\u2660') > Card('8', '\u2662'))
# print(Card('3', '\u2660') <= Card('8', '\u2662'))
# print(Card('3', '\u2660') >= Card('8', '\u2662'))

# 8.16
# class myInt(int):

#     def __init__(self, x):
#         self.x = x

#     def __add__(self, other):
#         print('Whatever ...')

# x = myInt(5)
# print(x * 4)
# print(x * (4 + 6))
# x + 6

# 8.17
# class myStr(str):
#     def __init__(self, string):
#         self.string = string

#     def __add__(self, other):
#         return (len(self) + len(other))

#     def __mul__(self, other):
#         return(len(self)*len(other))

# x = myStr('hello')
# print(x + 'universe')
# print(x * 'universe')

# 8.18
# class myList(list):
#     def sort(self):
#         print('You wish,,,')

# x = myList([1, 2, 3])
# print(x)
# x.reverse()
# print(x)
# print(x[2])
# x.sort()
