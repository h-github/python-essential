
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x[1]))
print(id(x))
print(id(y))
print(id(x[0]))
print(id(y[0]))

if x[0] is y[0]:
    print('Yep')
else:
    print('Nope')

if x is y:
    print('Yep')
else:
    print('Nope')


# not working if:
if type(x) == 'tuple':
    print('Yep')
else:
    print('Nope')

if isinstance(x, tuple):
    print('Yep')
else:
    print('Nope')


if isinstance(x, tuple):
    print('tuple')
elif isinstance(x, list):
    print('list')
else:
    print('Nope')


y = [1, 'two', 3.0, [4, 'four'], 5]
if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('Nope')

print('x is {}'.format(type(x)))
print('y is {}'.format(type(y)))
