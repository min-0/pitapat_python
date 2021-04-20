# 4.12
# s = 'abcdefghijklmnopqrstuvwxyz'
# print(s[:3])
# print(s[3:-2])
# print(s[-4:])
# print(s[-4:-1])

# 4.13
# s = 'abcdefghijklmnopqrstuvwxyz'
# print(s[1:2] == 'bc')  # b
# print(s[:14] == 'abcdefghijklmn')
# print(s[14:] == 'opqrstuvwxyz')
# print(s[1:-1] == 'bcdefghijklmnopqrstuvw')#bcdefghijklmnopqrstuvwy

# 4.14
# log = '128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "GET /docs/test.txt HTTP/1.0"'
# address = log.split()
# date = address[3]+address[4]

# 4.16
# fw, sw, lw = input().split()
# if(fw < sw and sw < lw):
#     print(True)

# 4.17
# message = 'The secret of this message is that it is secret'
# lenght = len(message)
# message.count('secret')
# censored = message.replace('secret', 'xxxxxx')
# print(censored)

# 4.18
# s = '''It was the best of times, it was the worst of times; it\n
# was the age of wisdom, it was the age of foolishness; it was the\n
# epoch of belief, it was the epoch of incredulity; it was...'''

# newS = s.replace('.', ' ')
# newS = s.replace(',', ' ')
# newS = s.replace(';', ' ')
# newS = s.replace('\n', ' ')

# newS.count('it was')
# print(newS.count('it was'))
# newS = newS.replace('was', 'is')
# listS = newS.split()
# print(newS)

# 4.19
# first = 'Marlena'
# last = 'Sigel'
# middle = 'Mae'
# print('{}, {} {}'.format(last, first, middle))
# print('{}, {} {}.'.format(last, first, middle[0]))
# print('{} {}. {}'.format(first, middle[0], last))
# print('{}. {}. {}'.format(middle[0], middle[0], last))
# print('{}, {}.'.format(last, middle[0]))

# 4.20
# sender = 'tim@abc.com'
# recipient = 'tom@xyz.org'
# subject = 'Hello!'
# print('From: {}\nTo: {}\nsubject: {}'.format(sender, recipient, subject))

# 4.21
# import math
# print(math.pi, math.e)
# print('pi:{:.1f}, e = {:.1f}'.format(math.pi, math.e))
# print('pi:{:.2f}, e = {:.2f}'.format(math.pi, math.e))
# print('pi:{:.6e}, e = {:.6e}'.format(math.pi, math.e))
# print('pi:{:.5f}, e = {:.5f}'.format(math.pi, math.e))
