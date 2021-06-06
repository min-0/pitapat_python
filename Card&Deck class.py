from random import random, shuffle

# 1단계


class Card:
    '게임용 카드를 표현하는 클래스'

    def __init__(self, rank, suit):
        '게임용 카드의 숫자패와 무늬패를 초기화'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        '숫자패 반환'
        return self.rank

    def getSuit(self):
        '무늬패 반환'
        return self.suit

# card = Card('3', '\u2660')
# print(card.getRank())
# print(card.getSuit())

# 2단계


class Deck:
    '52 카드의 카드 덱 표현'

    # ranks와 suits는 Deck 클래스 변수
    ranks = {'2', '3', '4', '5', '6', '7', '8', '10', 'J', 'Q', 'K', 'A'}

    # suits는 4가지 무늬패를 나타내는 4개의 유니코드 부호 집합
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        '52 카드의 카드 덱 초기화'
        self.deck = []  # 처음에 카드 덱은 비어있음

        for suit in Deck.suits:
            for rank in Deck.ranks:
                # 주어진 숫자패와 무늬패의 Card를 카드 덱에 추가
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        '카드 덱 섞기'
        shuffle(self.deck)

    def dealCard(self):
        '카드 덱의 최상위로부터 카드를 나누어 줌(배출 및 반환)'
        return self.deck.pop()


deck = Deck()
deck.shuffle()
card = deck.dealCard()
print(card.getRank(), card.getSuit())
card = deck.dealCard()
print(card.getRank(), card.getSuit())
card = deck.dealCard()
print(card.getRank(), card.getSuit())
