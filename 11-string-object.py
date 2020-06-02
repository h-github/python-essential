#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper())
print('Hello, World.'.swapcase())
print('The result is: {}'.format(42 * 7))

print("""

The result is: 
{}


""".format(42 * 7))

s = 'The result is: {}'
print(s.format(42 * 7))


class MyString(str):
    def __str__(self):
        return self[::-1]


s = MyString('Hello, World.')
print(s)
