data = 10421

print('주민번호 = ', str(data).zfill(6))

print('생년월일 =', 2000 + (int)(data/10000), '년',
      (int)((data % 10000)/100), '월', (int)((data % 100)/1), '일')

string = "Hello World"  # 문자열에도 정수 0을 채울 수 있읍니다.
print(str(string).zfill(15))

# zfill 함수 말고 정수 0 채우는 방법
print('%06d' % data)  # 10진수 형태로 출력하되 6자리를 다 채워서 출력하라.
