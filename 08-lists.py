#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(game[1])
    print(game[1:5:2])
    print_list(game)

    # i = game.index('Scissors')
    # print(i)

    game.append('Computer')
    print_list(game)

    game.insert(2, '7Sang')
    print_list(game)

    # game.remove('7Sang')
    # print_list(game)

    # p = game.pop()
    # print(p)
    # print_list(game)

    # p = game.pop(3)
    # print(p)
    # print_list(game)

    # del game[2]
    # print(game[0:5:3])
    # del game[0:5:3]
    # print_list(game)

    print(' | '.join(game))

    print(len(game))

    gameTuple = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
    print_list(gameTuple)

    # Now a tuple works exactly like a list except that it's immutable,
    # and it's indicated by parentheses.
    # So when I run this, you can see it runs exactly the same.
    # But if I try to append, I'll get an error that says tuple object has no attribute append
    gameTuple.append('Computer')
    print_list(gameTuple)


def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


if __name__ == '__main__':
    main()
