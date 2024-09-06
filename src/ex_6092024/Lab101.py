#hierarachical

class A:
    def methodA(self):
        return "Method A"

class B(A):
    def methodB(self):
        return "Method B"

class C(A):
    def methodC(self):
        return "Method C"


class D(B,C):
    def methodD(self):
        return "Method D"

obj_d=D()
print(obj_d.methodA())
print(obj_d.methodB())
print(obj_d.methodC())
print(obj_d.methodD())

