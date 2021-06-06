class Representation:
    def __repr__(self):  # 겹지정 연산자
        return 'canonical string representation'

    def __str__(self):  # 문자열 생성자
        return 'Pretty string representation'

rep = Representation()
print(rep)
