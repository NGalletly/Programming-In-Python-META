# class A:
#     def b(self):
#         return "Function inside A"


# class B:
#     pass


# class C:
#     def b(self):
#         return "Function inside C"


# class D(B, C, A):
#     pass


# class D(C):
#     pass


# d = D()
# print(d.b())


# # function inside C


# class A:
#     def c(self):
#         return "Function inside A"


# class B(A):
#     def c(self):
#         return "Function inside B"


# class C(A, B):
#     pass


# class D(C):
#     pass


# d = D()
# # print(d.c())


# class A:
#     pass


# class B(A):
#     pass


# class C(B):
#     pass


# c = C()
# print(c.a())

a = 5


class A:
    a = 7
    pass


class B(A):
    pass


class C(B):
    pass


c = C()
print(c.a())
