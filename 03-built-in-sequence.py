x = [1, 2, 3, 4, 5]
y = x.copy()
y[2] = 42
for i in x:
    print(f'i is {i}')

print()

for i in y:
    print(f'i is {i}')

print()


x = (1, 2, 3, 4, 5)
# x[2] = 42 tuple is immutable type
for i in x:
    print(f'i is {i}')

print()

x = range(10)
for i in x:
    print(f'i is {i}')


print()

x = range(5, 10)
for i in x:
    print(f'i is {i}')

print()

x = range(2, 50, 5)
# x[2] = 42 range is immutable type like tuple
for i in x:
    print(f'i is {i}')


print()

x = list(range(5))
x[2] = 42
for i in x:
    print(f'i is {i}')


print()

x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i in x:
    print(f'i is {i}')

print()

x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
x['three'] = 42
for k, v in x.items():
    print(f'key: {k}, value: {v}')
