#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys


def main():
    try:
        x = 20/0  # int('Seven')
    except ValueError:
        print('Expect an intiger string')
    # except ZeroDivisionError:
    #     print('Don\'t divid by zero!')
    except:
        print(f'Unknown error: {sys.exc_info()}')
        print(f'Unknown error: {sys.exc_info()[1]}')
    else:
        print('Awesome!')
        print(x)


if __name__ == '__main__':
    main()
