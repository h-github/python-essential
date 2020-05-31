#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    if pet == 'bunny':
        continue

    if pet == 'cat':
        break
    print(pet)
else:
    print('That is all of the animals')

print()

for pet in animals:
    if pet == 'bunny':
        continue
    print(pet)
else:
    print('That is all of the animals')

print()

for pet in range(5):

    print(pet)
