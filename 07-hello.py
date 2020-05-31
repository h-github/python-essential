# def f1():
#     print('This is f1')

# f1()
# x = f1
# x()


# def f1():
#     def f2():
#         print('This is f2')
#     return f2


# x = f1()

# x()


def f1(f):
    def f2():
        print('This is before the function call')
        f()
        print('This is after the function call')
    return f2


# def f3():
#     print('This is f3')

# f3 = f1(f3)
# f3()
# Because this is so meta and self-referential and weird and recursive,
# instead there's a short cut for it, which simply looks like this.

@f1
def f3():
    print('This is f3')


f3()

# So it takes f3, this syntax here which is called a decorator,
# it takes the function which is defined directly after it,
# so the syntax is you have to have the decorator,
# followed directly by the function definition and
# it takes that function and it passes it as an argument to the decorator function and it returns and
# it assigns that name of f3 to the wrapper itself.
# And so now I can't call f3 directly,
# I can only call it through the wrapper and f3 now is wrapped inside that decorator function.
