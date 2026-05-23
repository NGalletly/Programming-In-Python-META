class a:
    num = 5


class b(a):
    num = 9


class c(b):
    pass


print(c.mro())
print(c.num)
print(help(c))
