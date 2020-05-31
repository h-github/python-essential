
from decimal import *

x = 7
print('x is {}'.format(x))
print(type(x))

x = 7 * 3
print('7 * 3 = {}'.format(x))
print(type(x))

x = 7 / 3
print('7 / 3 = {}'.format(x))
print(type(x))

x = 7 // 3
print('7 // 3 = {}'.format(x))
print(type(x))

x = 7 % 3
print('7 % 3 = {}'.format(x))
print(type(x))


x = .1 + .1 + .1 - .3
print('.1 + .1 + .1 - .3 = {}'.format(x))
print(type(x))


a = Decimal('.10')
b = Decimal('.30')
x = a+a+a-b
print('.1 + .1 + .1 - .3 = {}'.format(x))
print(type(x))
