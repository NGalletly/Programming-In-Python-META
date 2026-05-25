# class a:
#     num = 5


# class b(a):
#     num = 9


# class c(b):
#     pass


# print(c.mro())
# print(c.num)
# print(help(c))

# ***
# class A:
#     def b(self):
#         return "Function inside A"


# class B:
#     def b(self):
#         return "Function inside B"


# class C(B, A):
#     # def b(self):
#     #     return "Function inside C"

#     pass


# class D(C):
#     pass


# d = D()
# print(d.b())


class A:
    def c(self):
        return "Function inside A"


class B:
    def c(self):
        return "Function inside B"


class C(A, B):
    def c(self):
        return "Function inside C"


class D(A, C):
    pass


d = D()
print(d.c)
