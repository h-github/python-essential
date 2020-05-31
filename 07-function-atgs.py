

# def main():
#     myfunction(1, 2, 46)


# def myfunction(a, b, c=0):
#     print(a, b, c)


# if __name__ == "__main__":
#     main()


def main():
    x = 5
    print(id(x))
    myfunction(x)
    print(f'in main: x is {x}')


def myfunction(a):
    print(id(a))
    a = 3
    print(id(a))
    print(a)


if __name__ == "__main__":
    main()
