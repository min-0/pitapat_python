# 4.3
# forecast = "It will be a sunny day today"
# (a)
# print(forecast.count('day'))
# (b)
# weather = forecast.find('sunny')
# print(weather)
# (e)
# change = forecast.replace('sunny', 'cloudy')
# print(change)

# 4.4
# def even(n):
#     for i in range(n):
#         if(i % 2 == 0 or i % 3 == 0):
#             print(i, end=', ')
# n = int(input('>>'))
# even(n)

# 4.5
# first = 'John'
# last = 'Doe'
# street = 'Main Street'
# number = 123
# city = 'AnyCity'
# state = 'AS'
# zipcode = '09876'
# print('{} {}\n{} {}\n{}, {} {}'.format(
#     first, last, number, street, city, state, zipcode))

# 모듈
# def greothrates(n):
#     print(' i  i**2   i**3    2**i')
#     formatStr = '{0:2d} {1:6d} {2:6d} {3:6d}'
#     for i in range(2, n+1):
#         print(formatStr.format(i, i**2, i**3, 2**i))
# greothrates(12)

# 4.7
# import time
# t = time.localtime(1500000000)
# print(time.strftime('%A, %B %d %Y', t))
# print(time.strftime('%I:%M %p Central Daylight Time on %m/%d/%Y', t))
# print(time.strftime('I will meet you on %a %B %d at %I:%M %p.', t))
