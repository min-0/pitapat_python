# 8.1
# class Point:
#    def getx(self):
#        return self.x

# 8.2
# class Test:
#    version = 1.02

#a = Test()
#b = Test()

# print(a.version)
# print(b.version)
# print(Test.version)
#Test.version = 1.03
# print(a.version)
# print(Test.version)
#a.version = 'Latest!!'
# print(Test.version)
# print(b.version)
# print(a.version)

# 8.3
# class Rectangle:
#    def setSize(self, width, lenght):
#        self.width = width
#        self.lenght = lenght

#    def perimetet(self):
#        return self.width*2 + self.lenght*2

#    def area(self):
#        return self.width * self.lenght

#rectangle = Rectangle()
#rectangle.setSize(3, 4)
# print(rectangle.perimetet())
# print(rectangle.area())

# 8.4
# class Animal:
#     def __init__(self, species='animal', language='make sounds'):
#         self.species = species
#         self.language = language

#     def Speak(self):
#         print('I am a {} and I {}'.format(self.species, self.language))

# snoopy = Animal('dog', 'bark')
# snoopy.Speak()
# tweety = Animal('canary')
# tweety.Speak()
# animal = Animal()
# animal.Speak()

# 8.5
# from random import shuffle

# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def getRank(self):
#         return self.rank

#     def getSuit(self):
#         return self.suit


# class Deck:
#     ranks = {'2', '3', '4', '5', '6', '7', '8', '10', 'J', 'Q', 'K', 'A'}
#     suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

#     def __init__(self, cardList=None):
#         if cardList != None:
#             self.deck = cardList
#         else:
#             self.deck = []

#         for suit in Deck.suits:
#             for rank in Deck.ranks:
#                 self.deck.append(Card(rank, suit))

#     def shuffle(self):
#         shuffle(self.deck)

#     def dealCard(self):
#         return self.deck.pop()


# deck = Deck(['1', '2', '3', '4'])
# deck.shuffle()
# print(deck.dealCard())
# card = deck.dealCard()
# print(card.getRank(), card.getSuit())

# 8.6
# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def getRank(self):
#         return self.rank

#     def getSuit(self):
#         return self.suit

#     def __repr__(self):
#         return "Card('{}', '{}')".format(self.rank, self.suit)
#         # 왜 'Card({}, {})'은 안되는거지 ? => 선언 해놓은 형식대로 해야 함

#     def __eq__(self, other):
#         return self.rank == other.rank and self.suit == other.suit


# print(Card('3', '\u2660') == Card('3', '\u2660'))
# print(Card('3', '\u2660') == eval(repr(Card('3', '\u2660'))))

# 8.7
# from random import shuffle


# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def getRank(self):
#         return self.rank

#     def getSuit(self):
#         return self.suit


# class Deck:
#     ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
#     suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

#     def __init__(self, deck=None):
#         self.deck = []

#         if deck != None:
#             self.deck = deck
#         else:
#             for suit in Deck.suits:
#                 for rank in Deck.ranks:
#                     self.deck.append(Card(rank, suit))

#     def shuffle(self):
#         shuffle(self.deck)

#     def dealCard(self):
#         return self.deck.pop(0)

#     def __eq__(self, other):
#         return self.deck == other.deck

#     def __len__(self):
#         return len(self.deck)

#     def __repr__(self):
#         return "Deck('{}')".format(self.deck)


# deck = Deck()
# print(len(deck))
# print(deck == deck)
# print(deck == eval(repr(deck)))

# 8.9
# class Queue:
#     def __init__(self):
#         self.q = []

#     def enqueue(self, item):
#         return self.q.append(item)

#     def isEmpty(self):
#         return(len(self.q) == 0)

#     def dequeue(self):
#         '''큐 맨 앞의 항목을 제거하고 반환
#             만약 큐가 비어있으면 KeyboardInterrupt 예외가 발생'''
#         if len(self) == 0:
#             raise KeyboardInterrupt('dequeue from empty queue')

#         return self.q.pop(0)

# queue = Queue()
# queue.dequeue()
