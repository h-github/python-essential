#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    # animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
    #            'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr',
                   giraffe='I am a giraffe!', dragon='rawr')
    print_dict(animals)

    print()

    for k in animals.keys():
        print(k)

    print()

    for v in animals.values():
        print(v)

    print()

    print(animals['puppy'])

    print()

    animals['lion'] = "I'm a lion"
    print_dict(animals)

    print()

    animals['monkey'] = "haha"
    print_dict(animals)

    print()

    print('lion' in animals)
    print('found!' if 'lion' in animals else 'nope!')

    print()

    # print(animals['godzilla']) # I get an error because godzilla doesn't exist
    print(animals.get('godzilla'))  # I get None because godzilla doesn't exist


def print_dict(o):
    for k, v in o.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()
