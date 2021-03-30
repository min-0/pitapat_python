# 실습문제 3.10

def noVowel(s):
    for c in s:
        if c in 'aiueoAIUEO':
            return False
    return True


s = (input("문자열을 입력하세요>> "))
print(noVowel(s))
