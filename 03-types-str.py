# x = 'seven "{1:>09}" "{0:>09}"'.format(8, 90)
a = 8
b = 9
x = f'seven {a} {b:>9}'
print('x is {}'.format(x))
print(type(x))
