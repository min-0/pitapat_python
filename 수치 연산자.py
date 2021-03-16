birth_date = "010421"

print('주민번호 = ' + birth_date)

data = 10421

print('생년월일 =', 2000 + (int)(data/10000), '년',
      (int)((data % 10000)/100), '월', (int)((data % 100)/1), '일')

# 2000년생 부터는 숫자로 년도를 받으면 0이 사라지고 오류가 생겨서,,,, 99일 때와 01일 때를 각각 짜보았읍니다 ^^

birthday = 990421

print('주민번호 =', birthday)
print('생년월일 =', 1900 + (int)(birthday/10000), '년',
      (int)((birthday % 10000)/100), '월', (int)((birthday % 100)/1), '일')
