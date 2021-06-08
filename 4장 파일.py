# 4.8
# def stringCount(filename, target):
#     '파일 filename의 target 빈도수 반환'
#     infile = open(filename, 'r')
#     content = infile.read()
#     infile.close()

#     print(content.count(target))


# stringCount('Test.txt', 'line')

# 4.9
# def words(filename):
#     '파일 filename의 단어 리스트 반환'
#     infile = open(filename, 'r')
#     content = infile.read()
#     infile.close()

#     table = str.maketrans('!,.:;?', 6*' ')
#     content = content.translate(table)
#     content = content.lower()

#     print(content.split())

# words('Test.txt')

# # 4.10
# def myGrep(filename, target):
#     '파일 filename에서 문자열 target이 포함된 라인 출력'
#     infile = open(filename, 'r')
#     for line in infile:
#         if target in line:
#             print(line, end='')

# myGrep('Test.txt', 'character')
