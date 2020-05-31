x = 5
y = x

print(id(x))
print(id(y))

print()

y = 3

print(id(x))
print(id(y))

print()

z = [1, 4, 3, 25]
w = z

print(z)
print(w)
print(id(z))
print(id(w))

print()

w[1] = 10

print(z)
print(w)
print(id(z))
print(id(w))

# So when you assign a mutable, you're actually assigning a reference to the mutable,
# and I have the side effect that when I change an element of that list in one place,
# it gets changed in both places because it's really just one object, and functions work exactly the same way.
