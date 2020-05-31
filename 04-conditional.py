#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

if True:
    print('if true')
elif False:
    print('elif true')
else:
    print('neither true')


if False:
    print('if true')
elif False:
    print('elif 1 true')
elif False:
    print('elif 2 true')
elif True:
    print('elif 3 true')
elif False:
    print('elif 4 true')
else:
    print('neither true')


# works like a switch in other languages
x = 5
if x == 0:
    print('if true')
elif x == 1:
    print('elif 1 true')
elif x == 2:
    print('elif 2 true')
elif x == 3:
    print('elif 3 true')
elif x == 4:
    print('elif 4 true')
elif x == 5:
    print('elif 5 true')
else:
    print('none true')
