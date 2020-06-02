
# https://docs.python.org/3/library/stdtypes.html#string-methods

print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.capitalize())
print('hello, world.'.title())
print('Hello, World.'.swapcase())
print('Hello, World.'.isspace())
print(' '.isspace())
print('Hello, World. Straße'.casefold())
print('Hello, World. Straße'.lower())


s1 = 'Hello, World.'
s2 = s1.upper()
# The upper method here has not just transformed the string in place.
# Rather, it's created a new object and returned that.
print(id(s1))
print(id(s2))

s2 = 'This is another string.'

print(s1 + ' ' + s2)
