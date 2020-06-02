
# https://docs.python.org/3/library/string.html#format-string-syntax

x = 42
print('The number is: {}'.format(x))

y = 73
print('The numbers are: {} {}'.format(x, y))
print('The numbers are: {m} {n}'.format(m=x, n=y))  # by variable
print('The numbers are: {n} {m}'.format(m=x, n=y))
print('The numbers are: {0} {1}'.format(x, y))  # by position
print('The numbers are: {1} {0}'.format(x, y))  # by position

print('The numbers are: {0} {1} {0}'.format(x, y))

print('The numbers are: {0:<5} {1:>5}'.format(x, y))
print('The numbers are: {0:<5} {1:+5}'.format(x, y))
print('The numbers are: {0:<5} {1:+05}'.format(x, y))

x = 42 * 747000
print('The number is: {}'.format(x))
print('The number is: {:,}'.format(x))
print('The number is: {:,}'.format(x).replace(',', '.'))  # for Europian
print('The number is: {:f}'.format(x))
print('The number is: {:.2f}'.format(x))


x = 42
print('The number is: {:b}'.format(x))  # binary


print(f'The number is: {x}')
print(f'The number is: {x:.3f}')
