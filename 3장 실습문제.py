# 3장 실습문제 3.1
# fahrenheit = eval(input('Enter the temperature in degrees Fahrenheit: '))
# celsius = 5/9 * (fahrenheit-32)
# print('The temperature in degrees Celsius is', celsius)

# 3.2 (a)
# age = eval(input('age: '))
# if(age >= 62):
#     print('You can get ypur pension benefits')
# (b)
# lst = ['Musial', 'Aaraon', 'Williams', 'Gehrin', 'Ruth']
# name = input('Your name: ')
# if(name in lst):
#     print('One of the top 5 baseball players, ever!')
# # (c)
# hits = eval(input('hits: '))
# shield = eval(input('shield: '))
# if(hits > 10 & shield == 0):
#     print('You are dead...')

# 3.3
# year = eval(input('year: '))
# if year % 4 == 0:
#     print('Could be a leap year.')
# else:
#     print('Definitely not a leap year.')

# 3.4
# ID = input('id>>')
# lst = ['joe', 'shu', 'hani', 'shphie']
# if ID in lst:
#     print('Login: ' + ID)
#     print('You are in!')
# else:
#     print('Login: ' + ID)
#     print('User unknow.')
# print('Done.')

# 3.5
wordList = input('Ender word list:').split()
for word in wordList:
    if len(word) == 4:
        print(word)
