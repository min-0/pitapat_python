# class Queue:
#     '고전적 큐 클래스'

#     def __init__(self):
#         '큐 항목들을 포함할 빈 리스트 생성함'
#         self.q = []

#     def dequeue(self):
#         '큐의 앞에서 항목을 제거하고 반환'
#         return self.q.pop(0)

#     def enqueue(self, item):
#         '큐의 제일 뒤에 항목 추가'
#         return self.q.append(item)

#     def isEmpty(self):
#         '큐가 비어있으면 True, 아니면 False 반환'
#         return(len(self.q) == 0)


# fruit = Queue()
# fruit.enqueue('apple')
# fruit.enqueue('banana')
# fruit.enqueue('coconut')

# print(fruit.dequeue())
# print(fruit.dequeue())
# print(fruit.dequeue())
# print(fruit.isEmpty())

class Queue:
    def __init__(self, q=None):
        '리스트 q를 기반으로 한 queue 초기화, 기본은 빈 큐'
        if q == None:
            self.q = []
        else:
            self.q = q

    def dequeue(self):
        '큐의 앞에서 항목을 제거하고 반환'
        return self.q.pop(0)

    def enqueue(self, item):
        '큐의 제일 뒤에 항목 추가'
        return self.q.append(item)

    def isEmpty(self):
        '큐가 비어있으면 True, 아니면 False 반환'
        return(len(self.q) == 0)

    def __eq__(self, other):
        '만약에 큐 self와 other가 같은 순서로 같은 항목을 포함한다면 True 반환'
        return self.q == other.q

    def __len__(self):
        '큐의 항목 수 반환'
        return len(self.q)

    def __repr__(self):
        '큐의 표준 문자열 표현 반환'
        return 'Queue({})'.format(self.q)


fruit = Queue()
fruit.enqueue('apple')
fruit.enqueue('banana')
fruit.enqueue('coconut')

print(fruit)
